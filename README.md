# Dynamic QR Code System on a Shoestring 🎯

A **zero-cost**, self-hosted dynamic QR code redirect system using **Quarto**, **Python**, **GitHub Pages**, and **Markdown as a database**. Update redirect destinations without regenerating QR codes!

## 🌟 Features

- **Static QR Codes**: Generate once, use forever—QR codes never change
- **Dynamic Redirects**: Update destinations by editing Markdown files
- **Zero Cost**: Fully hosted on GitHub Pages (free tier)
- **Auto-Deploy**: Push changes → GitHub Actions rebuilds site automatically
- **No Server Required**: Pure static site with client-side redirects
- **Full Control**: Own your data, own your infrastructure

## 🏗️ How It Works

1. **QR codes point to static URLs**: `yourusername.github.io/repo/{slug}`
2. **Markdown files define redirects**: Each file in `_redirects/` contains a `slug` and `target_url`
3. **Quarto renders redirect pages**: Generates HTML with meta refresh and JavaScript redirects
4. **GitHub Actions auto-builds**: Every commit triggers a site rebuild
5. **Users scan → redirect**: QR code → static URL → instant redirect to current target

```
┌─────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  QR Code    │ --> │  GitHub Pages    │ --> │  Target URL     │
│  /menu      │     │  /menu/index.html│     │  example.com/... │
└─────────────┘     └──────────────────┘     └─────────────────┘
     Static              Auto-rebuilt            Editable in MD
```

## 📁 Project Structure

```
.
├── _quarto.yml                 # Quarto configuration
├── _redirects/                 # Markdown "database" of redirects
│   ├── menu.qmd               # Redirect: /menu → target_url
│   ├── contact.qmd            # Redirect: /contact → target_url
│   └── promo.qmd              # Redirect: /promo → target_url
├── _extensions/
│   └── redirect/
│       ├── redirect.html      # HTML template for redirects
│       └── _extension.yml     # Extension config
├── .github/
│   └── workflows/
│       └── publish.yml        # GitHub Actions auto-deploy
├── generate_qr_codes.py       # Python script to generate QR codes
├── requirements.txt           # Python dependencies
├── index.qmd                  # Homepage
└── qr_codes/                  # Generated QR code images (not in repo)
```

## 🚀 Quick Start

### Prerequisites

- GitHub account
- Python 3.8+ (for QR code generation)
- Git

### 1. Clone and Set Up Repository

```bash
# Clone this repository
git clone https://github.com/yourusername/Dynamic-QR-code-on-a-shoestring.git
cd Dynamic-QR-code-on-a-shoestring

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install Python dependencies
pip install -r requirements.txt
```

### 2. Enable GitHub Pages

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Pages**
3. Under **Source**, select:
   - **Source**: Deploy from a branch
   - **Branch**: `gh-pages` / `root`
4. Click **Save**

### 3. Configure GitHub Actions Permissions

1. Go to **Settings** → **Actions** → **General**
2. Scroll to **Workflow permissions**
3. Select **Read and write permissions**
4. Check **Allow GitHub Actions to create and approve pull requests**
5. Click **Save**

### 4. Create Your First Redirect

Edit `_redirects/menu.qmd`:

```yaml
---
title: "Redirecting to Menu..."
slug: menu
target_url: "https://example.com/your-actual-menu"
format:
  html:
    template: ../_extensions/redirect/redirect.html
---
```

### 5. Generate QR Codes

```bash
# Replace with your actual GitHub Pages URL
python generate_qr_codes.py https://yourusername.github.io/Dynamic-QR-code-on-a-shoestring

# QR codes will be saved to qr_codes/ folder
```

### 6. Push and Deploy

```bash
git add .
git commit -m "Initial setup with redirects"
git push origin main
```

GitHub Actions will automatically:
- Build your Quarto site
- Deploy to GitHub Pages
- Make redirects live in ~1-2 minutes

### 7. Test Your Redirect

Visit: `https://yourusername.github.io/Dynamic-QR-code-on-a-shoestring/menu`

You should be redirected to your `target_url`!

## 📝 Adding New Redirects

### Step 1: Create a New Markdown File

Create `_redirects/newslug.qmd`:

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

### Step 2: Generate QR Code

```bash
python generate_qr_codes.py https://yourusername.github.io/Dynamic-QR-code-on-a-shoestring
```

### Step 3: Commit and Push

```bash
git add _redirects/newslug.qmd
git commit -m "Add newslug redirect"
git push
```

The QR code at `qr_codes/newslug.png` is now permanent—print it, share it, use it anywhere!

## 🔄 Updating Redirect Destinations

**This is the magic**: Change where a QR code points **without regenerating it**!

### Step 1: Edit the Markdown File

Edit `_redirects/menu.qmd`:

```yaml
---
title: "Redirecting to Menu..."
slug: menu
target_url: "https://example.com/new-menu-location"  # ← Changed!
format:
  html:
    template: ../_extensions/redirect/redirect.html
---
```

### Step 2: Commit and Push

```bash
git add _redirects/menu.qmd
git commit -m "Update menu redirect to new location"
git push
```

**That's it!** Within 1-2 minutes:
- GitHub Actions rebuilds the site
- `/menu` now redirects to the new URL
- Your existing QR codes work with the new destination
- No QR code regeneration needed!

## 🛠️ Customization

### Customize Redirect Page Appearance

Edit `_extensions/redirect/redirect.html` to change:
- Loading message
- Spinner animation
- Colors and styling
- Fallback link text

### Customize QR Code Appearance

Edit `generate_qr_codes.py` to adjust:
- Error correction level
- Box size
- Border width
- Colors (fill/background)

Example:

```python
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # Higher correction
    box_size=15,  # Larger boxes
    border=2,     # Smaller border
)
```

### Add Analytics

Add tracking to `_extensions/redirect/redirect.html`:

```html
<script>
  // Log redirect event
  console.log('Redirecting from: $slug$');
  console.log('Redirecting to: $target_url$');
  
  // Add your analytics code here
  // e.g., Google Analytics, Plausible, etc.
</script>
```

## 🎯 Use Cases

- **Restaurant Menus**: Update menu links seasonally without reprinting QR codes
- **Event Registration**: Change registration forms for recurring events
- **Product Links**: Update product pages without changing packaging
- **Contact Information**: Update contact forms or vCards
- **Promotional Campaigns**: Rotate promotional landing pages
- **Documentation**: Keep printed materials pointing to latest docs

## 🔧 Troubleshooting

### GitHub Actions Failing

**Check workflow permissions**:
1. Settings → Actions → General
2. Workflow permissions → Read and write permissions

**Check Pages settings**:
1. Settings → Pages
2. Source should be `gh-pages` branch

### Redirects Not Working

**Verify file structure**:
- Markdown files must be in `_redirects/` folder
- Must have `.qmd` extension
- Must include `slug` and `target_url` in frontmatter

**Check build logs**:
1. Go to Actions tab
2. Click latest workflow run
3. Check for errors in build step

### QR Codes Not Generating

**Verify Python environment**:
```bash
# Activate virtual environment
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

**Check file paths**:
- Script must be run from project root
- `_redirects/` folder must exist

## 📊 GitHub Actions Workflow

The workflow (`.github/workflows/publish.yml`) automatically:

1. **Triggers** on every push to `main` branch
2. **Checks out** your repository
3. **Sets up** Quarto
4. **Renders** the site (converts `.qmd` to HTML)
5. **Uploads** the `_site` folder as an artifact
6. **Deploys** to GitHub Pages

**View workflow runs**: Repository → Actions tab

## 🔐 Security Notes

- All redirects are public (GitHub Pages is public)
- Don't store sensitive URLs in redirect targets
- Consider using URL shorteners for additional privacy
- QR codes are permanent—choose slugs carefully

## 📚 Learn More

- [Quarto Documentation](https://quarto.org/docs/websites/)
- [GitHub Pages Documentation](https://docs.github.com/pages)
- [GitHub Actions for Quarto](https://github.com/quarto-dev/quarto-actions)
- [QRCode Python Library](https://github.com/lincolnloop/python-qrcode)

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 💡 Tips & Best Practices

1. **Choose meaningful slugs**: Use short, memorable slugs like `menu`, `contact`, `promo`
2. **Test before printing**: Always test redirects before printing QR codes
3. **Keep a backup**: Document your slug → purpose mapping
4. **Use descriptive commits**: Makes tracking changes easier
5. **Monitor analytics**: Track which QR codes get the most scans
6. **Set up notifications**: Get alerts when Actions fail

## 🎉 Success!

You now have a fully functional, zero-cost dynamic QR code system!

**Next steps**:
- Generate your QR codes
- Print and distribute them
- Update redirect targets anytime by editing Markdown files
- Watch GitHub Actions automatically deploy your changes

---

**Built with** ❤️ **using Quarto, Python, and GitHub Pages**