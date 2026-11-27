"""Test-only renderer whose text goes through ctx.rich() with a glossary term, a long formula and display math, and
which links a domain to a question card through ctx.question_anchor(): the build must accept it."""


def render(data, ctx):
    text = ctx.rich('Placeholder text naming the local vacuum, with '
                    '\\(\\Phi:B_{\\mathrm{ord}}(A_{\\mathrm{ch}})\\to C(\\mathcal F)\\) and \\[x^2+y^2=z^2\\]')
    q = ctx.question_anchor('d-native-interface')
    link = f'<a class="atlas-fixture-q" href="{q}">Placeholder question link</a>' if q else ''
    return {'html': f'<div class="atlas-fixture"><p class="atlas-fixture-text">{text}</p>{link}</div>'}
