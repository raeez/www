"""Test-only renderer whose script contains a closing script tag (the build must refuse it)."""


def render(data, ctx):
    return {'html': '<div class="atlas-fixture">Placeholder</div>', 'js': 'var s = "</script>";'}
