# System Architecture

## Overview

This document explains how the dynamic QR code system works under the hood.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                         USER WORKFLOW                            │
└─────────────────────────────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│  1. Edit Markdown File (_redirects/menu.qmd)                    │
│     ---                                                          │
│     slug: menu                                                   │
│     target_url: https://example.com/new-menu                    │
│     ---                                                          │
└─────────────────────────────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│  2. Git Commit & Push                                           │
│     $ git add _redirects/menu.qmd                               │
│     $ git commit -m "Update menu"                               │
│     $ git push origin main                                      │
└─────────────────────────────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│  3. GitHub Actions Triggered (.github/workflows/publish.yml)    │
│     - Checkout repository                                       │
│     - Setup Quarto                                              │
│     - Render site (quarto render)                               │
│     - Deploy to gh-pages branch                                 │
└─────────────────────────────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│  4. Quarto Build Process                                        │
│     Input:  _redirects/menu.qmd                                 │
│     Template: _extensions/redirect/redirect.html                │
│     Output: _site/menu/index.html                               │
└─────────────────────────────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│  5. GitHub Pages Deployment                                     │
│     Published: https://username.github.io/repo/menu             │
└─────────────────────────────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│  6. User Scans QR Code                                          │
│     QR Code → https://username.github.io/repo/menu              │
└─────────────────────────────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│  7. Browser Redirect                                            │
│     <meta http-equiv="refresh" content="0; url=target_url" />   │
│     <script>window.location.href = "target_url"</script>        │
└─────────────────────────────────────────────────────────────────┘
                                 │
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│  8. Final Destination                                           │
│     User arrives at: https://example.com/new-menu               │
└─────────────────────────────────────────────────────────────────┘
```

## Component Breakdown

### 1. Markdown Files (Database)

**Location**: `_redirects/*.qmd`

**Purpose**: Store redirect mappings in version-controlled files

**Structure**:
```yaml
---
title: "Redirecting..."
slug: menu              # URL path component
target_url: "https://..." # Destination URL
format:
  html:
    template: ../_extensions/redirect/redirect.html
---
```

**Why Markdown?**
- Human-readable
- Git-friendly (easy diffs)
- No database server needed
- Version controlled

### 2. Quarto Rendering Engine

**Location**: Quarto CLI (installed by GitHub Actions)

**Purpose**: Convert `.qmd` files to HTML pages

**Process**:
1. Read frontmatter (YAML metadata)
2. Apply template (`redirect.html`)
3. Substitute variables (`$slug$`, `$target_url$`)
4. Output static HTML to `_site/`

**Configuration**: `_quarto.yml`

### 3. Redirect Template

**Location**: `_extensions/redirect/redirect.html`

**Purpose**: HTML template for redirect pages

**Key Features**:
- Meta refresh tag (HTTP-level redirect)
- JavaScript redirect (client-side fallback)
- Loading spinner (visual feedback)
- Manual link (fallback for disabled JS)

**Template Variables**:
- `$slug$` - Replaced with slug value
- `$target_url$` - Replaced with target URL

### 4. GitHub Actions Workflow

**Location**: `.github/workflows/publish.yml`

**Triggers**:
- Push to `main` branch
- Manual workflow dispatch

**Steps**:
1. **Checkout**: Clone repository
2. **Setup**: Install Quarto
3. **Render**: Build site (`quarto render`)
4. **Upload**: Package `_site/` as artifact
5. **Deploy**: Push to `gh-pages` branch

**Deployment Target**: GitHub Pages

### 5. QR Code Generator

**Location**: `generate_qr_codes.py`

**Purpose**: Create static QR code images

**Process**:
1. Scan `_redirects/` for `.qmd` files
2. Extract `slug` from frontmatter
3. Generate QR code pointing to `{base_url}/{slug}`
4. Save as `qr_codes/{slug}.png`

**Important**: QR codes are generated **once** and never change!

### 6. GitHub Pages

**Purpose**: Host static site (free)

**Configuration**:
- Source: `gh-pages` branch
- Custom domain: Optional

**URL Format**: `https://username.github.io/repo-name/`

## Data Flow

### Creating a New Redirect

```
User creates .qmd file
    ↓
Runs generate_qr_codes.py
    ↓
QR code saved locally
    ↓
Commits and pushes
    ↓
GitHub Actions builds site
    ↓
Deployed to GitHub Pages
    ↓
QR code now functional
```

### Updating a Redirect

```
User edits .qmd file (changes target_url)
    ↓
Commits and pushes
    ↓
GitHub Actions rebuilds site
    ↓
New redirect deployed
    ↓
QR code now points to new destination
    ↓
NO QR code regeneration needed!
```

### User Scanning QR Code

```
User scans QR code
    ↓
Opens: https://username.github.io/repo/slug
    ↓
Browser loads HTML page
    ↓
Meta refresh triggers (0 second delay)
    ↓
JavaScript redirect executes (fallback)
    ↓
User arrives at target_url
```

## File Structure

```
Dynamic-QR-code-on-a-shoestring/
│
├── _quarto.yml                 # Quarto project config
├── _metadata.yml               # Global metadata
├── index.qmd                   # Homepage
├── styles.css                  # Custom styles
│
├── _redirects/                 # Redirect definitions
│   ├── menu.qmd               # Example: menu redirect
│   ├── contact.qmd            # Example: contact redirect
│   └── promo.qmd              # Example: promo redirect
│
├── _extensions/                # Quarto extensions
│   └── redirect/
│       ├── _extension.yml     # Extension config
│       └── redirect.html      # Redirect template
│
├── .github/
│   ├── workflows/
│   │   ├── publish.yml        # Auto-deploy workflow
│   │   └── test.yml           # Test workflow
│   └── ISSUE_TEMPLATE/        # Issue templates
│
├── generate_qr_codes.py       # QR code generator
├── requirements.txt           # Python dependencies
│
├── qr_codes/                  # Generated QR codes (local only)
│   ├── menu.png
│   ├── contact.png
│   └── promo.png
│
└── _site/                     # Built site (auto-generated)
    ├── index.html
    ├── menu/
    │   └── index.html         # Redirect page
    ├── contact/
    │   └── index.html
    └── promo/
        └── index.html
```

## Technology Stack

### Core Technologies

- **Quarto**: Static site generator
- **Python**: QR code generation
- **GitHub Actions**: CI/CD automation
- **GitHub Pages**: Free hosting

### Python Libraries

- `qrcode`: QR code generation
- `PyYAML`: YAML parsing
- `Pillow`: Image processing

### Web Technologies

- HTML5 meta refresh
- JavaScript redirects
- CSS3 animations

## Security Considerations

### Public by Default

- All redirects are public
- GitHub Pages sites are public
- Anyone can view redirect mappings

### No Authentication

- No login required
- No API keys needed
- Fully open system

### Best Practices

1. Don't use for sensitive URLs
2. Don't include credentials in target URLs
3. Consider URL shorteners for privacy
4. Monitor for unauthorized changes (git history)

## Scalability

### Limits

- **GitHub Pages**: 1GB site size, 100GB bandwidth/month
- **QR Codes**: Unlimited (generated locally)
- **Redirects**: Hundreds to thousands (no practical limit)

### Performance

- **Build Time**: ~30 seconds for 100 redirects
- **Redirect Speed**: <100ms (meta refresh)
- **Deployment**: 1-2 minutes (GitHub Actions)

## Advantages

1. **Zero Cost**: Completely free
2. **No Server**: Pure static hosting
3. **Version Control**: Full git history
4. **Auto-Deploy**: Push to deploy
5. **No Database**: Markdown files
6. **Portable**: Easy to migrate

## Limitations

1. **Public Only**: Can't have private redirects
2. **Build Delay**: 1-2 minute deployment time
3. **No Analytics**: Requires external tools
4. **Static Only**: No server-side logic

## Future Enhancements

Potential improvements:

- Analytics integration
- Redirect expiration dates
- A/B testing support
- Custom redirect rules
- Password protection
- Redirect categories/tags

---

**This architecture provides a simple, reliable, and cost-effective dynamic QR code system.**
