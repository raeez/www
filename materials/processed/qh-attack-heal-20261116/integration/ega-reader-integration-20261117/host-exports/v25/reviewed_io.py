"""Unchanged selected I/O primitives from the previously reviewed installer core."""
from __future__ import annotations
import contextlib
import ctypes
import datetime as dt
import fcntl
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys
import uuid
sys.dont_write_bytecode = True
HASH = re.compile(r'[0-9a-f]{64}\Z')

class GuardError(RuntimeError):
    pass


def require(condition, message):
    if not condition:
        raise GuardError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def enc(value):
    return (json.dumps(value, indent=2, ensure_ascii=False) + '\n').encode('utf-8')


def no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, 'duplicate JSON key: ' + key)
        result[key] = value
    return result


def decode(raw):
    return json.loads(raw.decode('utf-8'), object_pairs_hook=no_duplicate_keys)


def utc_now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def path_abs(value):
    require(isinstance(value, str) and value and Path(value).is_absolute(), 'an absolute path is required')
    require(str(Path(os.path.normpath(value))) == value, 'non-normalized path: ' + value)
    return Path(value)


def relative(value):
    require(isinstance(value, str) and value, 'empty relative path')
    p = Path(value)
    require(not p.is_absolute() and all(x not in ('', '.', '..') for x in value.split('/')),
            'unsafe relative path: ' + value)
    return p


def below(path, parent):
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def identity(st):
    return (st.st_dev, st.st_ino, st.st_mode, st.st_size, st.st_mtime_ns, st.st_ctime_ns)


def read_stable(path):
    """Reject endpoint symlinks, special files and replacement/in-place races."""
    path = Path(path)
    before = path.lstat()
    require(stat.S_ISREG(before.st_mode), 'not a regular non-symlink file: ' + str(path))
    with path.open('rb') as stream:
        opened = os.fstat(stream.fileno())
        raw = stream.read()
        finished = os.fstat(stream.fileno())
    after = path.lstat()
    require(identity(before) == identity(opened) == identity(finished) == identity(after)
            and len(raw) == after.st_size, 'file changed during read: ' + str(path))
    return raw


def pin(path, raw=None):
    path = Path(path)
    raw = read_stable(path) if raw is None else raw
    return {'path': str(path), 'sha256': sha(raw), 'bytes': len(raw)}


def valid_pin(value):
    require(isinstance(value, dict), 'pin must be an object')
    path_abs(value.get('path'))
    require(isinstance(value.get('sha256'), str) and HASH.fullmatch(value['sha256']),
            'pin needs a full lowercase SHA-256: ' + str(value.get('path')))
    require(type(value.get('bytes')) is int and value['bytes'] >= 0,
            'pin needs an exact byte count: ' + value['path'])
    return value


def check_pin(value):
    valid_pin(value)
    raw = read_stable(value['path'])
    require(sha(raw) == value['sha256'] and len(raw) == value['bytes'], 'pin drift: ' + value['path'])
    return raw


def assert_safe_directory(path):
    """Write destinations may not be redirected by a symlinked ancestor."""
    for parent in [path] + list(path.parents):
        if parent.exists() or parent.is_symlink():
            require(parent.is_dir() and not parent.is_symlink(), 'unsafe write directory: ' + str(parent))


def write_new(path, raw, mode=0o444):
    path = Path(path)
    assert_safe_directory(path.parent)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as stream:
        stream.write(raw)
        stream.flush()
        os.fsync(stream.fileno())
    path.chmod(mode)
    require(read_stable(path) == raw, 'new file did not retain exact bytes: ' + str(path))


def exchange_paths(left, right):
    """Atomic exchange keeps displaced bytes available for the post-swap guard."""
    libc = ctypes.CDLL(None, use_errno=True)
    if sys.platform == 'darwin' and hasattr(libc, 'renameatx_np'):
        fn, cwd = libc.renameatx_np, -2
    elif sys.platform.startswith('linux') and hasattr(libc, 'renameat2'):
        fn, cwd = libc.renameat2, -100
    else:
        raise GuardError('atomic rename exchange unavailable; unsafe replacement fallback is disabled')
    fn.argtypes = [ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_uint]
    fn.restype = ctypes.c_int
    if fn(cwd, os.fsencode(left), cwd, os.fsencode(right), 2) != 0:
        error = ctypes.get_errno()
        raise OSError(error, os.strerror(error), str(left))


def fsync_directory(path):
    fd = os.open(path, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def exchange_guarded(path, expected, replacement, displaced_dir, event, held_locks=None):
    """No os.replace fallback. Preserve and inspect the actual displaced inode."""
    path, displaced_dir = Path(path), Path(displaced_dir)
    require(read_stable(path) == expected, 'pre-exchange drift: ' + str(path))
    mode = stat.S_IMODE(path.stat().st_mode)
    temp = path.with_name('.' + path.name + '.frontier-' + uuid.uuid4().hex + '.tmp')
    write_new(temp, replacement, mode)
    candidate_lock = temp.open('rb')
    fcntl.flock(candidate_lock.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    if held_locks is not None:
        held_locks.append(candidate_lock)
    swap_in_effect = False
    try:
        require(read_stable(path) == expected, 'drift before atomic exchange: ' + str(path))
        event({'event': 'exchange_intent', 'path': str(path), 'temporary': str(temp),
               'before_sha256': sha(expected), 'after_sha256': sha(replacement)})
        exchange_paths(path, temp)
        swap_in_effect = True
        fsync_directory(path.parent)
        displaced = read_stable(temp)
        if displaced != expected:
            # A non-cooperating writer won the last instant. Restore its bytes if
            # our candidate is still current. Otherwise preserve both versions.
            if read_stable(path) == replacement:
                exchange_paths(path, temp)
                swap_in_effect = False
                event({'event': 'racing_writer_restored', 'path': str(path),
                       'restored_sha256': sha(displaced), 'displaced_candidate': str(temp)})
                if read_stable(temp) != replacement and read_stable(path) == displaced:
                    exchange_paths(path, temp)
                    event({'event': 'recovery_race_restored', 'path': str(path),
                           'retained_previous_version': str(temp)})
            else:
                event({'event': 'racing_writer_requires_root_recovery', 'path': str(path),
                       'preserved_displaced_file': str(temp), 'preserved_sha256': sha(displaced)})
            raise GuardError('atomic exchange detected concurrent modification; all displaced bytes retained: ' + str(path))
        require(read_stable(path) == replacement, 'concurrent modification immediately after exchange: ' + str(path))
        displaced_dir.mkdir(parents=True, exist_ok=True)
        backup = displaced_dir / (uuid.uuid4().hex + '--' + path.name)
        # Exclusive hard-link creation retains the actual old inode. Never
        # remove somebody else's path or overwrite a pre-existing archive file.
        os.link(temp, backup, follow_symlinks=False)
        require(os.lstat(temp).st_ino == os.lstat(backup).st_ino, 'displaced inode link mismatch')
        os.unlink(temp)
        event({'event': 'exchange_complete', 'path': str(path), 'displaced': str(backup),
               'displaced_sha256': sha(displaced), 'installed_sha256': sha(replacement)})
        return pin(backup, displaced)
    except BaseException:
        if swap_in_effect and temp.exists():
            # This also handles an I/O failure after exchange but before the
            # caller can journal completion. Restore only our own live bytes.
            try:
                if read_stable(path) == replacement:
                    restored = read_stable(temp)
                    exchange_paths(path, temp)
                    swap_in_effect = False
                    event({'event': 'failed_exchange_restored', 'path': str(path),
                           'restored_sha256': sha(restored), 'retained_displaced': str(temp)})
                    if read_stable(temp) != replacement:
                        # A second writer raced recovery itself. Its displaced
                        # bytes are restored if the recovery result is current.
                        if read_stable(path) == restored:
                            exchange_paths(path, temp)
                            event({'event': 'recovery_race_restored', 'path': str(path),
                                   'retained_previous_version': str(temp)})
            except (OSError, GuardError) as recovery_error:
                event({'event': 'failed_exchange_requires_root_recovery', 'path': str(path),
                       'temporary': str(temp), 'error': str(recovery_error)})
        # An orphaned temp is evidence, not garbage to discard during a failure.
        if temp.exists():
            event({'event': 'temporary_retained', 'path': str(temp)})
        raise
    finally:
        if held_locks is None:
            fcntl.flock(candidate_lock.fileno(), fcntl.LOCK_UN)
            candidate_lock.close()


@contextlib.contextmanager
def locked_targets(paths):
    handles = []
    try:
        for path in sorted(paths):
            stream = open(path, 'rb')
            handles.append(stream)
            try:
                fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            except OSError as exc:
                raise GuardError('another cooperating writer holds a target lock: ' + path) from exc
            require(stat.S_ISREG(os.fstat(stream.fileno()).st_mode), 'target lock opened a non-regular file')
        yield handles
    finally:
        for stream in reversed(handles):
            with contextlib.suppress(OSError):
                fcntl.flock(stream.fileno(), fcntl.LOCK_UN)
            stream.close()

