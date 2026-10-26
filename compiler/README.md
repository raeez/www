# Raeez.com article builds

The repository contains maintained root HTML pages and separate article builders.
Select the source route from its configuration before changing or regenerating a page.

## Source routes

`docs.config.js` configures the Google Docs importer in `build.js`.
It writes pages and an Atom feed under `compiler/dist/`.
That feed discovers pages in `dist/`. It does not replace the maintained root `feed.xml`.

`reader-papers.json` identifies the retained Markdown inputs for `build-reader-papers.py`.
The builder verifies source hashes and writes the corresponding HTML pages at the repository root.
Read `../references/source-provenance.md` before changing these source relationships.
Keep retained raw sources unchanged.

Run the reader-paper commands from the repository root:

```bash
python3 compiler/build-reader-papers.py
python3 compiler/build-reader-papers.py --check
```

The check requires Pandoc. It compares rendered HTML with the checked-in pages without writing them.
Inspect source dates and build diagnostics separately. A successful build does not establish external-source freshness.

## Quick Start

Run the following commands from `compiler/`:

```bash
# Install dependencies
npm install

# Build all configured imports locally
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
2. Edit only the assigned maintained source.
3. Run the applicable local build and checks.
4. Inspect the intended output and its publication exclusions.
5. Deploy only with current publication authorization.

Build time depends on source retrieval and document size.

## Troubleshooting

### "Document not found"
- Check the Google Doc is publicly accessible (Share → Anyone with link)
- Verify the doc ID in `docs.config.js`

### Content not updating
- Verify the source route first.
- For Google Docs imports, run `npm run build:force` to clear the cache.
- Inspect diagnostics for failed retrieval and stale-cache fallback.

### Styling issues
- Check Adobe Fonts kit ID is correct
- Verify the kit includes the necessary weights (400, 600)
