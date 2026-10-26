# Raeez.com local article builds

The repository contains maintained root HTML pages and separate article builders.
Select the source route from its configuration before changing or regenerating a page.

## Maintained sources

The root HTML essays are maintained locally.
The five public entries in `docs.config.js` use `localHtml` paths, so a build copies those pages into `dist/`.
Their Google Docs identifiers record their historical source routes.
The remote documents have not been checked for current content or modification dates.

The seven reader essays and guides use paired Markdown and TeX sources in `content/reader-papers/`.
For an authorized source change, edit both formats and review the changed claims.
Update their hashes in `compiler/reader-papers.json` before building.
Run these commands from the repository root:

```bash
python3 compiler/build-reader-papers.py
python3 compiler/build-reader-papers.py --check
```

The builder verifies maintained source hashes and the archived hashes in `references/reader-paper-snapshot.json` before rendering.
The check requires Pandoc. It compares rendered HTML with the checked-in pages without writing them.
Keep `materials/raw/2026-09-09-accessible-papers/` unchanged.
Read `../references/source-provenance.md` before changing these source relationships.
Inspect source dates and build diagnostics separately. A successful build does not establish external-source freshness.

The root `feed.xml` contains full articles and seven reader-paper summary entries.
The nine author-essay entries contain their maintained full text.
Synchronize only existing full-article entries, preserving the seven summaries and publication dates:

```bash
python3 compiler/sync-article-feed.py --updated 2026-10-22T00:00:00Z licc sez-in-a-box smart-buildings prefabricated-construction archai moxie
python3 compiler/sync-article-feed.py --check licc sez-in-a-box smart-buildings prefabricated-construction archai moxie
```

Use the actual editorial date for `--updated`.
The legacy feed generated in `dist/` discovers only pages in that directory.
Keep that feed separate from the maintained root `feed.xml`.

## Author essays

Nine author essays use Markdown in `content/author-essays/` and metadata in `compiler/author-essays.json`.
The builder verifies each maintained source, its archived input, and the unchanged article template before rendering.
Run these commands from the repository root:

```bash
python3 compiler/build-author-essays.py
python3 compiler/build-author-essays.py --check
```

An optional slug limits the command to one essay.
After an edit, synchronize its full-text feed entry with `python3 compiler/sync-article-feed.py --updated <actual-ISO-timestamp> <slug>`.
Check it with `python3 compiler/sync-article-feed.py --check <slug>`.
The pages use the existing article template and `reader-papers.css`. The build leaves both files unchanged.
Original month-only dates remain month-only. Record an exact publication date only when the source establishes one.

`licc-blueprint.html` is excluded from GitHub Pages and from the public compiler configuration.
Its exact adopted edition remains in excluded source custody under `materials/raw/2026-10-22-private-planning/`.
It previously appeared at a public URL and in the feed.
The October curation withdraws that public route while retaining `licc.html` as the public project essay.

## Historical Google Docs importer

`docs.config.js` configures `build.js`.
Entries without a `localHtml` path use the Google Docs importer and the article template.
Explicit fetch commands update the local import cache. They leave maintained root HTML unchanged.
The build writes pages and an Atom feed under `compiler/dist/`.

## Quick Start

Run the following commands from `compiler/`:

```bash
# Install dependencies
npm install

# Build configured documents locally
npm run build

# Build a single document
npm run build:one sez-in-a-box

# Clear the import cache and rebuild
npm run build:force

# Preview locally
npm run serve

# Build and preview
npm run dev
```

## Deployment

Deployment requires current publication authorization.
Both preview and production commands publish externally.
Review the target branch, host, and output directory before running them.
For GitHub Pages, preserve the exclusions in the repository-root `_config.yml`.

### Vercel

```bash
# Preview deploy
npm run deploy:preview

# Production deploy
npm run deploy
```

Connecting a repository for automatic deployment also requires publication authorization.

### Cloudflare Pages

1. Connect your GitHub repo
2. Set build command: `npm run build`
3. Set output directory: `dist`

### Manual / Other Hosts

For an authorized manual deployment, upload the reviewed output from the selected build route.

## Configuration

### Adobe Fonts Setup

`template.html` already loads an Adobe Fonts kit for Garamond Premier Pro.
It also loads EB Garamond as a fallback.
Inspect that configuration before changing the typography.
For an authorized replacement, use a kit with the required families and weights:

```html
<link rel="stylesheet" href="https://use.typekit.net/abc1def.css">
```

### Adding a New Document

1. Edit `docs.config.js`:

```javascript
{
  id: 'YOUR_GOOGLE_DOC_ID',
  slug: 'url-friendly-name',
  title: 'Document Title',
  subtitle: 'Document Subtitle',
  meta: 'Date — Version',
  metaLink: {
    text: 'View on Google Docs',
    url: 'https://docs.google.com/document/d/YOUR_ID'
  },
  description: 'SEO description for the document.',
  filterPatterns: [
    'TITLE TO REMOVE FROM BODY',
    'AUTHOR LINE TO REMOVE'
  ]
}
```

2. Run `npm run build`

### Filter Patterns

The `filterPatterns` array removes content from the document body that's already displayed in the header (title, subtitle, author, date). Patterns are case-insensitive and match anywhere in the text.

## Document Structure

Each document page includes:

- **Header**: Title, subtitle, metadata with optional link
- **Body**: Cleaned Google Docs content
- **Footer**: Author byline, navigation

## Caching

`build.js` reuses Google Docs content from `.cache/` for 24 hours.
If retrieval fails, it can use an older cached copy and report that fallback.
Use `npm run build:force` to clear the import cache before rebuilding.
Check retrieval diagnostics before reporting source freshness.

## File Structure

```
compiler/
├── build.js          # Main build script
├── docs.config.js    # Document configuration
├── template.html     # HTML template
├── package.json
├── README.md
├── .cache/           # Cached Google Docs HTML (gitignored)
└── dist/             # Generated static files (gitignored)
    ├── sez-in-a-box.html
    └── ...
```

## Typography Features

- Garamond Premier Pro (with EB Garamond fallback)
- Perfect fourth modular scale (1.333)
- 8px baseline grid
- Golden ratio spacing
- Old-style numerals
- Proper ligatures
- Optical margin alignment
- Automatic hyphenation

## LLM & SEO Indexability

Each page includes:

- Schema.org `ScholarlyArticle` structured data
- Semantic HTML with proper heading hierarchy
- Clean, crawlable text (no JavaScript rendering)
- Meta descriptions
- Canonical URLs

## Workflow

1. Identify the page's source route and preserve its provenance.
2. For entries with `localHtml`, edit the assigned maintained root HTML.
3. For reader or author essays, use the maintained source routes above.
4. Run the applicable local build and checks.
5. Inspect the intended output and its publication exclusions.
6. Deploy only with current publication authorization.

Build time depends on the source route, retrieval, and document size.

## Troubleshooting

### "Document not found"
- Check the Google Doc is publicly accessible (Share → Anyone with link)
- Verify the doc ID in `docs.config.js`

### Content not updating
- Verify the source route first.
- Check the configured `localHtml` source when present.
- For Google Docs imports, run `npm run build:force` to clear the cache.
- Inspect diagnostics for failed retrieval and stale-cache fallback.

### Styling issues
- Check Adobe Fonts kit ID is correct
- Verify the kit includes the necessary weights (400, 600)
