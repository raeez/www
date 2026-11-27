"""Test-only atlas renderer for the mount test. It exercises the AtlasContext interface and returns
placeholder markup; the real renderer is owned by the atlas lane (compiler/quantum-holography-status/atlas.py)."""
import html


def render(data, ctx):
    problems = []
    items = []
    for claim in data.get('claims', []):
        href = ctx.anchor_for(claim['id'])
        code = claim['status']['code']
        # The atlas's codes and the page's statuses: scoped_negative is the page's 'refuted form'. An unknown code is
        # refused, not drawn as open.
        page_status = {'checked': 'checked', 'conditional': 'conditional', 'remaining': 'open',
                       'scoped_negative': 'refuted form'}.get(code)
        if page_status is None:
            problems.append(f'claim {claim["id"]}: unknown status code {code!r}')
        # The label is the page's, selected by the stored code; the record's own status.label is a display alias.
        mark = ctx.mark(page_status, ctx.status_labels.get(page_status)) if page_status else ''
        title = ctx.rich(claim['title'], terms=False)
        link = f'<a href="{href}">{title}</a>' if href else title
        anchor = getattr(ctx, 'claim_anchor', None)  # the claim's own anchor, where the page's context offers it
        id_attr = f' id="{anchor(claim["id"])}"' if anchor else ''
        items.append(f'<li class="atlas-fixture-claim"{id_attr} data-claim="{html.escape(claim["id"])}">{mark} {link}</li>')
    domains = ''.join(f'<li>{html.escape(d["label"])}: {ctx.rich(d["summary"])}</li>' for d in data.get('domains', []))
    if not data.get('claims'):
        problems.append('no claims')
    body = (f'<div class="atlas-fixture" id="atlas-fixture-root"><ul class="atlas-fixture-domains">{domains}</ul>'
            f'<ul class="atlas-fixture-claims">{"".join(items)}</ul></div>')
    return {'html': body, 'title': 'Placeholder atlas', 'nav_label': 'Atlas',
            'css': '.atlas-fixture{border-top:1px solid var(--rule)}', 'js': 'window.__atlasFixtureRan = true;',
            'problems': problems}
