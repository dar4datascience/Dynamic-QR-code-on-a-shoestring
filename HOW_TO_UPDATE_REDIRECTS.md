# How to Update Redirects - Simple Guide

## The Simple Truth

Each `.qmd` file at the project root is a redirect page with a button. To change where it redirects, just **edit the URL in ONE place**.

## Example: Update Menu Redirect

### Current File (`menu.qmd`):

```html
<a href="https://example.com/restaurant-menu" 
   id="redirectButton"
   style="...">
  View Menu →
</a>
```

### To Change Redirect Destination:

**Find and replace the URL in ONE place:**

Look for the line with `<a href="..."` and change the URL:

```html
<a href="https://YOUR-NEW-URL" 
```

### Example - Change to New Menu:

**Before:**
```html
<a href="https://example.com/restaurant-menu" 
```

**After:**
```html
<a href="https://myrestaurant.com/new-menu-2024" 
```

## Quick Steps

1. **Open** the `.qmd` file you want to update (e.g., `menu.qmd`)
2. **Find** the button link: `<a href="https://example.com/..."`
3. **Replace** with your new URL
4. **Save** the file
5. **Commit and push**:
   ```bash
   git add menu.qmd
   git commit -m "Update menu to new URL"
   git push
   ```
6. **Wait** 1-2 minutes for GitHub Actions to rebuild

## That's It!

Your QR code will now redirect to the new URL. No QR code regeneration needed!

## File Structure

```
Project Root/
├── menu.qmd      → Redirects to your menu URL
├── contact.qmd   → Redirects to your contact URL
└── promo.qmd     → Redirects to your promo URL
```

When Quarto builds the site:
- `menu.qmd` becomes `_site/menu.html`
- QR code points to: `https://yourname.github.io/repo/menu`
- User sees a button and auto-redirects in 3 seconds

## How It Works

1. **User scans QR code** → Opens `yoursite.github.io/menu`
2. **Page loads** with a big button
3. **Countdown starts** (3 seconds)
4. **User can click button** to redirect immediately
5. **Or wait** for automatic redirect
6. **Arrives** at your target URL

The button URL is the **only thing you need to change** to update the redirect!
