# Raeez.com local article builds

## Maintained sources

The root HTML essays are maintained locally. The five public entries in `docs.config.js` use `localHtml` paths, so a build copies those pages into `dist/`. Their Google Docs identifiers record their historical source routes. The remote documents have not been checked for current content or modification dates.

The seven reader essays and guides use paired Markdown and TeX sources in `content/reader-papers/`. Edit both formats, review the changed claims, and update their hashes in `compiler/reader-papers.json` before building:

```bash
python3 compiler/build-reader-papers.py
python3 compiler/build-reader-papers.py --check
```

Run these commands from the repository root. The builder checks the archived source hashes in `references/reader-paper-snapshot.json` before rendering. Keep `materials/raw/2026-09-09-accessible-papers/` unchanged. See `references/source-provenance.md` for the source history.

The root `feed.xml` contains full articles and seven reader-paper summary entries. The nine author-essay entries contain their maintained full text. Synchronize only existing full-article entries, preserving the seven summaries and publication dates:

```bash
python3 compiler/sync-article-feed.py --updated 2026-10-22T00:00:00Z licc sez-in-a-box smart-buildings prefabricated-construction archai moxie
python3 compiler/sync-article-feed.py --check licc sez-in-a-box smart-buildings prefabricated-construction archai moxie
```

Use the actual editorial date for `--updated`. The legacy feed generated in `dist/` discovers only pages in that directory; it is not a replacement for the root feed.

## Author essays

Nine author essays use Markdown in `content/author-essays/` and metadata in `compiler/author-essays.json`. The builder verifies each maintained source, its archived input, and the unchanged article template before rendering:

```bash
python3 compiler/build-author-essays.py
python3 compiler/build-author-essays.py --check
```

An optional slug limits the command to one essay. After an edit, synchronize that full-text feed entry with `python3 compiler/sync-article-feed.py --updated <actual-ISO-timestamp> <slug>` and check it with `python3 compiler/sync-article-feed.py --check <slug>`. The pages use the existing article template and `reader-papers.css`; neither file is changed by the build. Original month-only dates remain month-only. An exact publication date is recorded only when the source establishes one.

`licc-blueprint.html` is excluded from GitHub Pages and from the public compiler configuration. Its exact adopted edition remains in excluded source custody under `materials/raw/2026-10-22-private-planning/`. It previously appeared at a public URL and in the feed; this curation withdraws that public route while retaining `licc.html` as the public project essay.

## Historical Google Docs importer

Entries without a `localHtml` path use the Google Docs importer and the article template. Explicit fetch commands update the local import cache; they do not change maintained root HTML.

## Architecture

```
Maintained root HTML (`localHtml`) or configured Google Docs import
       ↓
   Build Script (on-demand)
       ↓
   Static HTML (dist/)
       ↓
   CDN (Vercel/Cloudflare)
```

## Quick Start

```bash
# Install dependencies
npm install

# Build configured documents locally
npm run build

# Build a single document
npm run build:one sez-in-a-box

# Clear the import cache and build
npm run build:force

# Preview locally
npm run serve

# Build and preview
npm run dev
```

## Deployment

### Vercel (Recommended)

```bash
# Preview deploy
npm run deploy:preview

# Production deploy
npm run deploy
```

Or connect your GitHub repo to Vercel for automatic deployments.

### Cloudflare Pages

1. Connect your GitHub repo
2. Set build command: `npm run build`
3. Set output directory: `dist`

### Manual / Other Hosts

Just upload the contents of `dist/` to any static host.

## Configuration

### Adobe Fonts Setup

1. Go to [fonts.adobe.com](https://fonts.adobe.com)
2. Find "Adobe Garamond Pro"
3. Add to a Web Project
4. Copy your Kit ID
5. Replace `YOUR_KIT_ID` in `template.html`:

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

The build script caches Google Docs content for 1 hour in `.cache/`. Use `npm run build:force` to bypass the cache.

## File Structure

```
raeez-site/
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

- Adobe Garamond Pro (with EB Garamond fallback)
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

1. Edit the maintained root HTML for entries with `localHtml`.
2. Run the local build and inspect its output.
3. Deploy only with current publication authorization.

The build time depends on the source route and article size.

## Troubleshooting

### "Document not found"
- Check the Google Doc is publicly accessible (Share → Anyone with link)
- Verify the doc ID in `docs.config.js`

### Content not updating
- Check the configured `localHtml` source first.
- For an entry that imports Google Docs, use `npm run build:force` to clear the import cache.

### Styling issues
- Check Adobe Fonts kit ID is correct
- Verify the kit includes the necessary weights (400, 600)
