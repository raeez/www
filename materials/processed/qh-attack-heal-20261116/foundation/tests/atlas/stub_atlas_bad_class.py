"""Test-only renderer whose markup reuses a class that the page script binds (the build must refuse it)."""


def render(data, ctx):
    return {'html': '<div class="atlas-fixture"><article class="statement">Placeholder</article></div>'}
