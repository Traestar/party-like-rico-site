# Project Documentation

## Overview
This project is built with WordPress and Elementor.

## Folder Structure

```
assets/
  css/        — Custom stylesheets (enqueued via child theme or plugin)
  js/         — Custom JavaScript files
  fonts/      — Self-hosted web fonts

images/
  logos/      — Logo variations (SVG, PNG)
  banners/    — Hero and banner images
  icons/      — UI icons and favicons

docs/
  README.md                  — This file
  elementor-templates/       — Exported Elementor JSON templates (.json)
```

## Elementor Templates
Export templates from Elementor > My Templates and save the `.json` files in `docs/elementor-templates/` for version control.

## Custom Styles
Add custom CSS overrides in `assets/css/`. These can be loaded via:
- Elementor > Site Settings > Custom CSS
- A child theme's `functions.php` using `wp_enqueue_style()`

## Custom Scripts
Add JavaScript in `assets/js/`. Enqueue via child theme or a code snippet plugin.
