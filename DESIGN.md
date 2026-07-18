---
name: Verdant Table
colors:
  surface: '#f9f9fc'
  surface-dim: '#dadadc'
  surface-bright: '#f9f9fc'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f6'
  surface-container: '#eeeef0'
  surface-container-high: '#e8e8ea'
  surface-container-highest: '#e2e2e5'
  on-surface: '#1a1c1e'
  on-surface-variant: '#3d4949'
  inverse-surface: '#2f3133'
  inverse-on-surface: '#f0f0f3'
  outline: '#6d7a79'
  outline-variant: '#bcc9c8'
  surface-tint: '#006a6a'
  primary: '#006767'
  on-primary: '#ffffff'
  primary-container: '#008282'
  on-primary-container: '#f3fffe'
  inverse-primary: '#64d8d7'
  secondary: '#bc0005'
  on-secondary: '#ffffff'
  secondary-container: '#e3241a'
  on-secondary-container: '#fffbff'
  tertiary: '#7d5400'
  on-tertiary: '#ffffff'
  tertiary-container: '#9d6b00'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#82f5f4'
  primary-fixed-dim: '#64d8d7'
  on-primary-fixed: '#002020'
  on-primary-fixed-variant: '#004f4f'
  secondary-fixed: '#ffdad5'
  secondary-fixed-dim: '#ffb4a9'
  on-secondary-fixed: '#410000'
  on-secondary-fixed-variant: '#930003'
  tertiary-fixed: '#ffddaf'
  tertiary-fixed-dim: '#ffba43'
  on-tertiary-fixed: '#281800'
  on-tertiary-fixed-variant: '#614000'
  background: '#f9f9fc'
  on-background: '#1a1c1e'
  surface-variant: '#e2e2e5'
typography:
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '800'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 36px
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Work Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: auto
  max-width: 1280px
---

## Brand & Style

The brand personality for this design system is **vibrant, community-focused, and refreshingly clean**. It draws direct inspiration from the physical storefront of the restaurant, translating the architectural teal and bold signage into a digital presence that feels established yet energetic. 

The design style follows a **Corporate / Modern** aesthetic with a touch of **Minimalism**. It prioritizes high legibility and clear information hierarchy to serve a diverse family audience. By utilizing generous whitespace and crisp structural elements, the UI evokes a sense of hygiene and professional service, ensuring the food photography remains the focal point.

## Colors

The palette is anchored by a **Vibrant Teal** (#009B9B), pulled directly from the restaurant's primary facade. This color represents freshness and the "Green" in the brand name. 

- **Primary:** Teal is used for main actions, navigation headers, and primary branding elements.
- **Secondary:** A bold **Heritage Red** (#E2231A), inspired by the "Green Plate" signage and the Coca-Cola branding in the reference image, is used sparingly for highlights, sales tags, and critical calls-to-action.
- **Tertiary:** An **Ochre Yellow** (#F9B233) acts as an accent color for ratings and celebratory accents (balloons/special offers).
- **Neutral:** A range of clean whites and deep charcoals provide the necessary contrast for a professional food-service application.

## Typography

This design system utilizes a dual-font strategy to balance character with utility. 

**Plus Jakarta Sans** is used for headlines. Its soft, modern curves feel welcoming and optimistic, mirroring the "family" aspect of the restaurant. Heavy weights are preferred for main titles to emulate the physical 3D signage of the storefront.

**Work Sans** is used for all functional text, menus, and descriptions. Its professional and grounded nature ensures that dense food menus and pricing remain highly legible across all device types. Labels use an uppercase treatment with slight tracking to provide a rhythmic "signage" feel within the UI.

## Layout & Spacing

The layout follows a **Fluid Grid** model for mobile and tablet, transitioning to a **Fixed Grid** for desktop. 

- **Grid:** Use a 12-column grid for desktop (max-width 1280px) and a 4-column grid for mobile.
- **Rhythm:** An 8px base unit governs all spatial relationships. 
- **Margins:** Large 48px or 80px vertical sections are used to separate major content areas (e.g., Hero, Menu Categories, About Us) to maintain a high-end, uncluttered feel.
- **Density:** Menu items should use a generous `md` (24px) padding to allow users to easily scan prices and dish names without visual overwhelm.

## Elevation & Depth

Visual hierarchy is established primarily through **Tonal Layers** and **Low-Contrast Outlines**. 

To maintain the clean "Green Plate" aesthetic, avoid heavy, dark shadows. Instead:
- **Surface 0:** The main background is pure white (#FFFFFF).
- **Surface 1:** Card containers use a very subtle light gray background (#F8F9FA) with a 1px border (#E9ECEF).
- **Floating Elements:** Active states or "Order Now" sticky bars use a soft, ambient shadow with a hint of Teal tinting (e.g., `box-shadow: 0 10px 30px rgba(0, 155, 155, 0.08)`).
- **Interactive Depth:** On hover, cards should slightly lift and the border color should transition to the Primary Teal.

## Shapes

The shape language is **Rounded**, reflecting the friendly and approachable nature of a family establishment. 

- **Base Radius:** 0.5rem (8px) is the standard for cards and input fields.
- **Large Radius:** 1rem (16px) is reserved for featured sections, images, and major container blocks.
- **Pill Shapes:** Used exclusively for tags, chips (e.g., "Vegetarian", "Spicy"), and primary action buttons to make them feel "touchable" and friendly.

## Components

### Buttons
- **Primary:** Pill-shaped, Primary Teal background, White text. High-contrast and bold.
- **Secondary:** Pill-shaped, White background, Teal border, Teal text.
- **Ghost:** No background or border, used for secondary navigation or "Back" actions.

### Cards
- **Food Item Card:** Image at the top with a 16px radius, followed by the dish name in `headline-md`, price in `body-lg` (bold), and a small pill-shaped chip for dietary labels.
- **Category Card:** Uses the Teal background with White iconography and text to act as a visual anchor.

### Input Fields
- Understated design with a subtle border. On focus, the border thickens to 2px and changes to Primary Teal. Labels are always positioned above the field in `label-sm`.

### Chips / Badges
- Used for cuisine types (Indian, Chinese, Continental). These should look like the small white signs on the restaurant front: white background, thin border, and centered text in `label-md`.

### Lists
- Menu lists should include a faint dotted or solid line separator between the item name and price to guide the eye across the horizontal space.