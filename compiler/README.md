# Raeez.com Static Site Generator

A build system that fetches research papers from Google Docs and generates beautifully typeset static HTML using Adobe Garamond Pro.

## Architecture

```
Google Docs (source of truth)
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

# Build all documents
npm run build

# Build a single document
npm run build:one smart-assets

# Force rebuild (clear cache)
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
    ├── smart-assets.html
    ├── momentum-monograph.html
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

1. **Edit in Google Docs** — Your source of truth
2. **Run build** — `npm run build` when ready to publish
3. **Deploy** — `npm run deploy` or push to GitHub

The build takes ~2-3 seconds per document on first run (cached thereafter).

## Troubleshooting

### "Document not found"
- Check the Google Doc is publicly accessible (Share → Anyone with link)
- Verify the doc ID in `docs.config.js`

### Content not updating
- Run `npm run build:force` to clear cache
- Or delete `.cache/` manually

### Styling issues
- Check Adobe Fonts kit ID is correct
- Verify the kit includes the necessary weights (400, 600)
