# Example Use Cases

This folder contains example redirect configurations for common use cases.

## Restaurant Menu

**File**: `_redirects/menu.qmd`

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

**Use Case**: Print QR codes on table tents. Update menu seasonally without reprinting.

---

## Event Registration

**File**: `_redirects/register.qmd`

```yaml
---
title: "Redirecting to Registration..."
slug: register
target_url: "https://eventbrite.com/your-event-2024"
format:
  html:
    template: ../_extensions/redirect/redirect.html
---
```

**Use Case**: Annual events. Same QR code on posters, update URL each year.

---

## Contact Form

**File**: `_redirects/contact.qmd`

```yaml
---
title: "Redirecting to Contact..."
slug: contact
target_url: "https://forms.google.com/your-form"
format:
  html:
    template: ../_extensions/redirect/redirect.html
---
```

**Use Case**: Business cards with QR codes. Update form without reprinting cards.

---

## Product Information

**File**: `_redirects/product.qmd`

```yaml
---
title: "Loading Product Info..."
slug: product
target_url: "https://yourstore.com/product/item-123"
format:
  html:
    template: ../_extensions/redirect/redirect.html
---
```

**Use Case**: QR codes on product packaging. Update product pages without changing packaging.

---

## Social Media Links

**File**: `_redirects/social.qmd`

```yaml
---
title: "Redirecting..."
slug: social
target_url: "https://linktr.ee/yourprofile"
format:
  html:
    template: ../_extensions/redirect/redirect.html
---
```

**Use Case**: Link aggregator that can be updated. Print on marketing materials.

---

## WiFi Password

**File**: `_redirects/wifi.qmd`

```yaml
---
title: "Loading WiFi Info..."
slug: wifi
target_url: "https://yoursite.com/wifi-instructions"
format:
  html:
    template: ../_extensions/redirect/redirect.html
---
```

**Use Case**: Guest WiFi access. Update password page without changing QR code.

---

## Feedback Form

**File**: `_redirects/feedback.qmd`

```yaml
---
title: "Redirecting to Feedback..."
slug: feedback
target_url: "https://forms.google.com/feedback"
format:
  html:
    template: ../_extensions/redirect/redirect.html
---
```

**Use Case**: Customer feedback. Update form or survey tool without changing printed materials.

---

## Promotional Campaign

**File**: `_redirects/promo.qmd`

```yaml
---
title: "Loading Special Offer..."
slug: promo
target_url: "https://yourstore.com/spring-sale-2024"
format:
  html:
    template: ../_extensions/redirect/redirect.html
---
```

**Use Case**: Seasonal promotions. Same QR code, different campaigns throughout the year.

---

## Tips for Effective Use

1. **Choose memorable slugs**: Short and relevant to the purpose
2. **Test before printing**: Always verify redirects work before mass printing
3. **Document your slugs**: Keep a record of what each slug is used for
4. **Plan for longevity**: Consider how long the QR code will be in use
5. **Monitor usage**: Add analytics to track which codes are scanned most
