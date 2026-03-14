# Quick Start Guide

Get your dynamic QR code system running in **5 minutes**!

## Prerequisites

- GitHub account
- Python 3.8+
- Git installed

## Step-by-Step Setup

### 1️⃣ Clone & Install (2 minutes)

```bash
# Clone the repository
git clone https://github.com/YOUR-USERNAME/Dynamic-QR-code-on-a-shoestring.git
cd Dynamic-QR-code-on-a-shoestring

# Set up Python environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2️⃣ Configure GitHub (1 minute)

**Enable GitHub Pages:**
1. Go to **Settings** → **Pages**
2. Source: **Deploy from a branch**
3. Branch: **gh-pages** / **root**
4. Click **Save**

**Enable Actions:**
1. Go to **Settings** → **Actions** → **General**
2. Workflow permissions: **Read and write permissions**
3. Check ✓ **Allow GitHub Actions to create and approve pull requests**
4. Click **Save**

### 3️⃣ Edit Your First Redirect (30 seconds)

Edit `_redirects/menu.qmd`:

```yaml
---
title: "Redirecting to Menu..."
slug: menu
target_url: "https://YOUR-ACTUAL-WEBSITE.com/menu"  # ← Change this!
format:
  html:
    template: ../_extensions/redirect/redirect.html
---
```

### 4️⃣ Generate QR Codes (30 seconds)

```bash
# Replace with YOUR GitHub username and repo name
python generate_qr_codes.py https://YOUR-USERNAME.github.io/Dynamic-QR-code-on-a-shoestring
```

QR codes saved to `qr_codes/` folder! 🎉

### 5️⃣ Deploy (1 minute)

```bash
git add .
git commit -m "Initial setup"
git push origin main
```

Wait 1-2 minutes for GitHub Actions to deploy.

### 6️⃣ Test It!

Visit: `https://YOUR-USERNAME.github.io/Dynamic-QR-code-on-a-shoestring/menu`

You should be redirected to your target URL! ✅

## What You Just Created

- ✅ **3 sample redirects** (menu, contact, promo)
- ✅ **3 QR codes** (static, never change)
- ✅ **Auto-deployment** (push to update)
- ✅ **Zero cost hosting** (GitHub Pages)

## Next Steps

### Update a Redirect

1. Edit `_redirects/menu.qmd` → change `target_url`
2. `git add . && git commit -m "Update menu" && git push`
3. Wait 1-2 minutes → redirect updated!

### Add a New Redirect

1. Create `_redirects/newslug.qmd`:
   ```yaml
   ---
   title: "Redirecting..."
   slug: newslug
   target_url: "https://example.com/destination"
   format:
     html:
       template: ../_extensions/redirect/redirect.html
   ---
   ```

2. Generate QR code:
   ```bash
   python generate_qr_codes.py https://YOUR-USERNAME.github.io/REPO-NAME
   ```

3. Commit and push:
   ```bash
   git add .
   git commit -m "Add newslug redirect"
   git push
   ```

## Troubleshooting

**404 on GitHub Pages URL?**
- Wait 5 minutes for initial deployment
- Check Settings → Pages is enabled

**Actions failing?**
- Check Settings → Actions → Workflow permissions
- Verify `gh-pages` branch exists after first run

**QR codes not generating?**
- Activate virtual environment: `source venv/bin/activate`
- Reinstall: `pip install -r requirements.txt`

## Full Documentation

- [Complete README](README.md) - Full documentation
- [Setup Guide](SETUP_GUIDE.md) - Detailed setup instructions
- [Examples](examples/README.md) - Use case examples

---

**That's it!** You now have a fully functional dynamic QR code system. 🚀

**Print your QR codes and start using them today!**
