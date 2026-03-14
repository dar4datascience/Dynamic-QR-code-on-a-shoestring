# Complete Setup Guide

This guide walks you through setting up your dynamic QR code system from scratch.

## Table of Contents

1. [Initial Setup](#initial-setup)
2. [GitHub Configuration](#github-configuration)
3. [Local Development](#local-development)
4. [Creating Redirects](#creating-redirects)
5. [Generating QR Codes](#generating-qr-codes)
6. [Deployment](#deployment)
7. [Updating Redirects](#updating-redirects)

---

## Initial Setup

### 1. Fork or Clone Repository

**Option A: Fork (Recommended)**
1. Click the "Fork" button on GitHub
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Dynamic-QR-code-on-a-shoestring.git
   cd Dynamic-QR-code-on-a-shoestring
   ```

**Option B: Use as Template**
1. Click "Use this template" on GitHub
2. Create a new repository
3. Clone your new repository

### 2. Install Python Dependencies

```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # Linux/Mac
# OR
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt
```

---

## GitHub Configuration

### Step 1: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (top menu)
3. Click **Pages** (left sidebar)
4. Under **Build and deployment**:
   - **Source**: Deploy from a branch
   - **Branch**: Select `gh-pages` and `/root`
   - Click **Save**

> **Note**: The `gh-pages` branch will be created automatically by GitHub Actions on first deployment.

### Step 2: Configure Actions Permissions

1. In **Settings**, click **Actions** → **General**
2. Scroll to **Workflow permissions**
3. Select **Read and write permissions**
4. Check ✓ **Allow GitHub Actions to create and approve pull requests**
5. Click **Save**

### Step 3: Verify Actions are Enabled

1. In **Settings** → **Actions** → **General**
2. Under **Actions permissions**, ensure:
   - **Allow all actions and reusable workflows** is selected
3. Click **Save**

---

## Local Development

### Install Quarto (Optional, for local testing)

**Linux:**
```bash
wget https://github.com/quarto-dev/quarto-cli/releases/download/v1.4.549/quarto-1.4.549-linux-amd64.deb
sudo dpkg -i quarto-1.4.549-linux-amd64.deb
```

**Mac:**
```bash
brew install quarto
```

**Windows:**
Download installer from [quarto.org](https://quarto.org/docs/get-started/)

### Test Locally

```bash
# Render the site
quarto render

# Preview the site
quarto preview
```

Visit `http://localhost:4200` to see your site.

---

## Creating Redirects

### Redirect File Template

Create a new file in `_redirects/` folder:

**File**: `_redirects/yourslug.qmd`

```yaml
---
title: "Redirecting..."
slug: yourslug
target_url: "https://example.com/your-destination"
format:
  html:
    template: ../_extensions/redirect/redirect.html
---
```

### Field Descriptions

- **title**: Page title (shown briefly during redirect)
- **slug**: Short identifier used in URL (e.g., `menu`, `contact`)
- **target_url**: Destination URL (where users will be redirected)
- **format**: Must include the redirect template path

### Slug Naming Rules

✅ **Good slugs:**
- `menu`
- `contact`
- `promo-2024`
- `event-reg`

❌ **Avoid:**
- Spaces: `my menu` ❌
- Special characters: `menu!` ❌
- Very long: `restaurant-menu-winter-2024-special` ❌

### Example Redirects

**Restaurant Menu:**
```yaml
---
title: "Loading Menu..."
slug: menu
target_url: "https://yourrestaurant.com/menu"
format:
  html:
    template: ../_extensions/redirect/redirect.html
---
```

**Contact Form:**
```yaml
---
title: "Redirecting to Contact..."
slug: contact
target_url: "https://forms.google.com/your-form-id"
format:
  html:
    template: ../_extensions/redirect/redirect.html
---
```

**Event Registration:**
```yaml
---
title: "Redirecting to Registration..."
slug: register
target_url: "https://eventbrite.com/your-event"
format:
  html:
    template: ../_extensions/redirect/redirect.html
---
```

---

## Generating QR Codes

### Step 1: Determine Your GitHub Pages URL

Your URL format: `https://YOUR-USERNAME.github.io/REPO-NAME`

**Example:**
- Username: `johndoe`
- Repo: `Dynamic-QR-code-on-a-shoestring`
- URL: `https://johndoe.github.io/Dynamic-QR-code-on-a-shoestring`

### Step 2: Run the Generator

```bash
# Activate virtual environment
source venv/bin/activate

# Generate QR codes
python generate_qr_codes.py https://YOUR-USERNAME.github.io/REPO-NAME
```

**Example:**
```bash
python generate_qr_codes.py https://johndoe.github.io/Dynamic-QR-code-on-a-shoestring
```

### Step 3: Verify Generated QR Codes

```bash
ls qr_codes/
# Should show: menu.png, contact.png, promo.png, etc.
```

### Step 4: Test QR Codes

Use a QR code scanner app to test:
1. Scan the QR code
2. Verify it opens the correct URL format
3. Example: `https://johndoe.github.io/Dynamic-QR-code-on-a-shoestring/menu`

> **Important**: QR codes point to static URLs and never need regeneration!

---

## Deployment

### First Deployment

```bash
# Stage all files
git add .

# Commit
git commit -m "Initial setup: Add redirects and configuration"

# Push to GitHub
git push origin main
```

### Monitor Deployment

1. Go to your repository on GitHub
2. Click **Actions** tab
3. You should see a workflow running: "Publish Quarto Site to GitHub Pages"
4. Click on the workflow to see progress
5. Wait for ✅ green checkmark (usually 1-2 minutes)

### Verify Deployment

1. Visit: `https://YOUR-USERNAME.github.io/REPO-NAME`
2. You should see the homepage
3. Test a redirect: `https://YOUR-USERNAME.github.io/REPO-NAME/menu`
4. You should be redirected to your `target_url`

### Troubleshooting First Deployment

**404 Error on GitHub Pages URL:**
- Wait 5 minutes (initial deployment can be slow)
- Check Settings → Pages to ensure it's enabled
- Verify `gh-pages` branch exists

**Actions Workflow Failed:**
- Click on the failed workflow
- Read error messages
- Common issues:
  - Permissions not set correctly
  - Syntax error in `.qmd` files
  - Missing template reference

---

## Updating Redirects

### Scenario: Update Menu Link

**Current**: Menu points to `https://example.com/old-menu`  
**Goal**: Point to `https://example.com/new-menu`

### Step 1: Edit Redirect File

Edit `_redirects/menu.qmd`:

```yaml
---
title: "Loading Menu..."
slug: menu
target_url: "https://example.com/new-menu"  # ← Changed!
format:
  html:
    template: ../_extensions/redirect/redirect.html
---
```

### Step 2: Commit and Push

```bash
git add _redirects/menu.qmd
git commit -m "Update menu to new location"
git push origin main
```

### Step 3: Wait for Deployment

1. GitHub Actions automatically triggers
2. Site rebuilds in ~1-2 minutes
3. No QR code regeneration needed!

### Step 4: Verify

1. Scan your existing QR code (or visit the URL)
2. Confirm redirect goes to new destination

---

## Advanced Configuration

### Custom Domain

1. Add `CNAME` file to project root:
   ```
   yourdomain.com
   ```

2. Configure DNS:
   - Add CNAME record pointing to `YOUR-USERNAME.github.io`

3. In GitHub Settings → Pages:
   - Enter custom domain
   - Enable "Enforce HTTPS"

### Add Analytics

Edit `_extensions/redirect/redirect.html`:

```html
<script>
  // Google Analytics
  gtag('event', 'redirect', {
    'slug': '$slug$',
    'target': '$target_url$'
  });
</script>
```

### Customize Redirect Appearance

Edit `_extensions/redirect/redirect.html`:

```html
<style>
  .container {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
  }
</style>
```

---

## Maintenance

### Regular Tasks

**Weekly:**
- Check GitHub Actions for failed builds
- Verify critical redirects still work

**Monthly:**
- Review and update outdated redirects
- Check for broken target URLs

**As Needed:**
- Add new redirects for new campaigns
- Archive old redirects (keep files for history)

### Backup Strategy

```bash
# Export all redirect mappings
python -c "
import yaml
from pathlib import Path

redirects = {}
for file in Path('_redirects').glob('*.qmd'):
    with open(file) as f:
        content = f.read()
        if content.startswith('---'):
            fm = yaml.safe_load(content.split('---')[1])
            redirects[fm['slug']] = fm['target_url']

print(yaml.dump(redirects))
" > redirect_backup.yml
```

---

## Quick Reference

### File Structure
```
_redirects/yourslug.qmd    → Redirect definition
qr_codes/yourslug.png      → Generated QR code
_site/yourslug/index.html  → Built redirect page (auto-generated)
```

### URLs
```
QR Code Points To:  https://username.github.io/repo/slug
Redirects To:       [target_url from .qmd file]
```

### Commands
```bash
# Generate QR codes
python generate_qr_codes.py https://username.github.io/repo

# Local preview
quarto preview

# Deploy
git add . && git commit -m "message" && git push
```

---

## Getting Help

**Common Issues:**
- [Troubleshooting Guide](README.md#troubleshooting)
- [GitHub Actions Documentation](https://docs.github.com/actions)
- [Quarto Documentation](https://quarto.org/docs/)

**Community:**
- Open an issue on GitHub
- Check existing issues for solutions

---

**You're all set!** 🎉

Your dynamic QR code system is ready to use. Create redirects, generate QR codes, and update destinations anytime without reprinting!
