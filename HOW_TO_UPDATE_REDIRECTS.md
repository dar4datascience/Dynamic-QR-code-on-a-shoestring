# How to Update Redirects - Simple Guide

## The Simple Truth

Each `.qmd` file in `_redirects/` is a redirect page. To change where it redirects, just **edit the URL in two places**.

## Example: Update Menu Redirect

### Current File (`_redirects/menu.qmd`):

```yaml
---
title: "Redirecting to Menu..."
pagetitle: "Redirecting..."
---

```{=html}
<meta http-equiv="refresh" content="0; url=https://example.com/restaurant-menu" />
<script type="text/javascript">
  window.location.href = "https://example.com/restaurant-menu";
</script>

<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 70vh; text-align: center;">
  <h1>Redirecting to Menu...</h1>
  <div class="spinner"></div>
  <p>If you are not redirected automatically, <a href="https://example.com/restaurant-menu">click here</a>.</p>
</div>
<!-- ... spinner CSS ... -->
```

### To Change Redirect Destination:

**Find and replace the URL in 3 places:**

1. Line 7: `<meta http-equiv="refresh" content="0; url=YOUR-NEW-URL" />`
2. Line 9: `window.location.href = "YOUR-NEW-URL";`
3. Line 15: `<a href="YOUR-NEW-URL">click here</a>`

### Example - Change to New Menu:

```yaml
---
title: "Redirecting to Menu..."
pagetitle: "Redirecting..."
---

```{=html}
<meta http-equiv="refresh" content="0; url=https://myrestaurant.com/new-menu-2024" />
<script type="text/javascript">
  window.location.href = "https://myrestaurant.com/new-menu-2024";
</script>

<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 70vh; text-align: center;">
  <h1>Redirecting to Menu...</h1>
  <div class="spinner"></div>
  <p>If you are not redirected automatically, <a href="https://myrestaurant.com/new-menu-2024">click here</a>.</p>
</div>
<!-- ... spinner CSS ... -->
```

## Quick Steps

1. **Open** the `.qmd` file you want to update
2. **Find** the old URL (appears 3 times)
3. **Replace** all 3 instances with your new URL
4. **Save** the file
5. **Commit and push**:
   ```bash
   git add _redirects/menu.qmd
   git commit -m "Update menu to new URL"
   git push
   ```
6. **Wait** 1-2 minutes for GitHub Actions to rebuild

## That's It!

Your QR code will now redirect to the new URL. No QR code regeneration needed!

## File Structure

```
_redirects/
├── menu.qmd      → Redirects to your menu URL
├── contact.qmd   → Redirects to your contact URL
└── promo.qmd     → Redirects to your promo URL
```

When Quarto builds the site:
- `menu.qmd` becomes `_site/menu/index.html`
- QR code points to: `https://yourname.github.io/repo/menu`
- That page redirects to whatever URL you put in the file

## Pro Tip

Use find-and-replace in your editor to change all 3 URLs at once:
- Find: `https://example.com/restaurant-menu`
- Replace: `https://myrestaurant.com/new-menu`
- Replace All (3 occurrences)
