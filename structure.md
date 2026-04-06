  ---
  Party Like Rico — Elementor Layout Blueprint

  ---
  Section 1: Navigation Header

  Elementor Name: Header – Nav

  ┌───────────────────┬──────────────────┬──────────────────────────────────────────────────────────────┐
  │      Element      │      Widget      │                            Notes                             │
  ├───────────────────┼──────────────────┼──────────────────────────────────────────────────────────────┤
  │ Logo (text/image) │ Image or Heading │ Left-aligned                                                 │
  ├───────────────────┼──────────────────┼──────────────────────────────────────────────────────────────┤
  │ Nav menu          │ Nav Menu widget  │ Home, Events, Media, Promote, Contact (dropdown), Blog, Shop │
  ├───────────────────┼──────────────────┼──────────────────────────────────────────────────────────────┤
  │ Tickets CTA       │ Button           │ Gold accent, right side                                      │
  └───────────────────┴──────────────────┴──────────────────────────────────────────────────────────────┘

  Structure: 1 Section → 1 Row → 3 Columns (Logo / Nav / Button)

  ---
  Section 2: Hero

  Elementor Name: Hero – Main Banner

  ┌─────────────────────┬──────────────────┬──────────────────────────────────────────────────────┐
  │       Element       │      Widget      │                        Notes                         │
  ├─────────────────────┼──────────────────┼──────────────────────────────────────────────────────┤
  │ Background          │ Section BG image │ Dark gradient overlay                                │
  ├─────────────────────┼──────────────────┼──────────────────────────────────────────────────────┤
  │ H1 Headline         │ Heading          │ "420 Weekend AC"                                     │
  ├─────────────────────┼──────────────────┼──────────────────────────────────────────────────────┤
  │ Subheading          │ Text Editor      │ Event tagline                                        │
  ├─────────────────────┼──────────────────┼──────────────────────────────────────────────────────┤
  │ Icon + detail pills │ Icon List        │ Date, Location, Time, Age, Shuttle, Gifts            │
  ├─────────────────────┼──────────────────┼──────────────────────────────────────────────────────┤
  │ CTA Buttons         │ Button (x2)      │ "Buy Tickets" (gold) + "View Full Details" (outline) │
  └─────────────────────┴──────────────────┴──────────────────────────────────────────────────────┘

  Structure: 1 Full-width Section → 1 Column, centered content

  ---
  Section 3: Ticker Strip

  Elementor Name: Ticker – Announcement Bar

  ┌────────────────┬───────────────┬──────────────────────────────┐
  │    Element     │    Widget     │            Notes             │
  ├────────────────┼───────────────┼──────────────────────────────┤
  │ Scrolling text │ HTML widget   │ CSS marquee/ticker animation │
  ├────────────────┼───────────────┼──────────────────────────────┤
  │ Background     │ Gold gradient │ #d4a017 → #f0bf3a            │
  └────────────────┴───────────────┴──────────────────────────────┘

  Structure: 1 narrow full-width Section → 1 Column → HTML widget

  ---
  Section 4: Flagship Event

  Elementor Name: Featured – Flagship Event Card

  ┌──────────────────┬───────────────┬─────────────────────────────────────────────────┐
  │     Element      │    Widget     │                      Notes                      │
  ├──────────────────┼───────────────┼─────────────────────────────────────────────────┤
  │ Section label    │ Heading       │ "April 18, 2026 - Flagship Event"               │
  ├──────────────────┼───────────────┼─────────────────────────────────────────────────┤
  │ Event card box   │ Inner Section │ Bordered card, dark bg                          │
  ├──────────────────┼───────────────┼─────────────────────────────────────────────────┤
  │ Event title      │ Heading       │ "420 Weekend AC Bud Crawl"                      │
  ├──────────────────┼───────────────┼─────────────────────────────────────────────────┤
  │ Description      │ Text Editor   │ Paragraph copy                                  │
  ├──────────────────┼───────────────┼─────────────────────────────────────────────────┤
  │ Icon detail list │ Icon List     │ Date, Check-in, Departure, Location, Age, Gifts │
  ├──────────────────┼───────────────┼─────────────────────────────────────────────────┤
  │ CTA Buttons      │ Button (x2)   │ "Buy Tickets Now" + "Full Event Details"        │
  ├──────────────────┼───────────────┼─────────────────────────────────────────────────┤
  │ Support text     │ Text Editor   │ Phone number                                    │
  └──────────────────┴───────────────┴─────────────────────────────────────────────────┘

  Structure: 1 Section → 1 Column → Inner Section card (centered, max-width ~700px)

  ---
  Section 5: Upcoming Events Grid

  Elementor Name: Events – Upcoming Grid

  ┌───────────────────┬───────────────────────────────────────┬────────────────────────────────────────────────────┐
  │      Element      │                Widget                 │                       Notes                        │
  ├───────────────────┼───────────────────────────────────────┼────────────────────────────────────────────────────┤
  │ Section heading   │ Heading                               │ "What's Next — Upcoming Events"                    │
  ├───────────────────┼───────────────────────────────────────┼────────────────────────────────────────────────────┤
  │ "See All Events"  │ Button (text style)                   │ Right-aligned                                      │
  │ link              │                                       │                                                    │
  ├───────────────────┼───────────────────────────────────────┼────────────────────────────────────────────────────┤
  │ 6 Event cards     │ Repeater via Loop Grid or manual      │ Each card: icon badge, title, date, description,   │
  │                   │ Inner Sections                        │ location, CTA                                      │
  └───────────────────┴───────────────────────────────────────┴────────────────────────────────────────────────────┘

  Structure: 1 Section → Heading row → 3-column grid (2 rows of 3 cards)

  Each card contains:
  - Badge (icon + category label)
  - Event title (Heading)
  - Date (Text)
  - Description (Text Editor)
  - Location (Icon List, single item)
  - CTA Button

  ---
  Section 6: Limited Spots CTA Banner

  Elementor Name: CTA – Urgency Banner

  ┌─────────────────┬─────────────┬──────────────────────────────────────────┐
  │     Element     │   Widget    │                  Notes                   │
  ├─────────────────┼─────────────┼──────────────────────────────────────────┤
  │ Headline        │ Heading     │ "Don't Miss Out."                        │
  ├─────────────────┼─────────────┼──────────────────────────────────────────┤
  │ Supporting copy │ Text Editor │ Paragraph                                │
  ├─────────────────┼─────────────┼──────────────────────────────────────────┤
  │ CTA Buttons     │ Button (x2) │ "Buy Tickets Now" + "View Event Details" │
  └─────────────────┴─────────────┴──────────────────────────────────────────┘

  Structure: 1 Full-width Section (dark/gold bg) → 1 Column, centered

  ---
  Section 7: Why Choose Us

  Elementor Name: Features – Why Party Like Rico

  ┌─────────────────┬──────────────────────┬─────────────────────────────────┐
  │     Element     │        Widget        │              Notes              │
  ├─────────────────┼──────────────────────┼─────────────────────────────────┤
  │ Section heading │ Heading              │ "Why Party Like Rico"           │
  ├─────────────────┼──────────────────────┼─────────────────────────────────┤
  │ 6 Feature boxes │ Icon Box widget (x6) │ Icon + title + description each │
  └─────────────────┴──────────────────────┴─────────────────────────────────┘

  Structure: 1 Section → Heading row → 3-column row (x2) with Icon Box widgets

  Feature boxes:
  1. Curated 420 Experiences
  2. Shuttle Party Format
  3. Atlantic City Roots
  4. VIP Giveaways
  5. Community Built
  6. Real Promotion

  ---
  Section 8: Experience Categories

  Elementor Name: Categories – What We Do

  ┌──────────────────┬───────────────────┬──────────────────────────────────────┐
  │     Element      │      Widget       │                Notes                 │
  ├──────────────────┼───────────────────┼──────────────────────────────────────┤
  │ Section heading  │ Heading           │ "What We Do — Experience Categories" │
  ├──────────────────┼───────────────────┼──────────────────────────────────────┤
  │ 6 Category cards │ Icon Box (linked) │ Each links to /events                │
  └──────────────────┴───────────────────┴──────────────────────────────────────┘

  Structure: 1 Section → Heading row → 3-column grid (x2 rows)

  Categories: 420 Events, Nightlife, Vendor Pop-Ups, Private Celebrations, Community Events, Shore Experiences

  ---
  Section 9: Partner / Sponsorship CTA

  Elementor Name: CTA – Partner With Us

  ┌─────────────┬─────────────────────┬────────────────────────────────────────┐
  │   Element   │       Widget        │                 Notes                  │
  ├─────────────┼─────────────────────┼────────────────────────────────────────┤
  │ Heading     │ Heading             │ "Partner With Us"                      │
  ├─────────────┼─────────────────────┼────────────────────────────────────────┤
  │ Subheading  │ Heading (H3)        │ "Get Your Brand at Our Events"         │
  ├─────────────┼─────────────────────┼────────────────────────────────────────┤
  │ Copy        │ Text Editor         │ Paragraph                              │
  ├─────────────┼─────────────────────┼────────────────────────────────────────┤
  │ CTA Buttons │ Button (x2)         │ "Become a Vendor" + "Sponsorship Info" │
  ├─────────────┼─────────────────────┼────────────────────────────────────────┤
  │ Stats       │ Counter widget (x2) │ 500+ Attendees / 12+ Events            │
  └─────────────┴─────────────────────┴────────────────────────────────────────┘

  Structure: 1 Section → 1 or 2 columns (text left, stats right)

  ---
  Section 10: Testimonials

  Elementor Name: Social Proof – Testimonials

  ┌─────────────────────┬─────────────────────────────────────────┬────────────────────────────┐
  │       Element       │                 Widget                  │           Notes            │
  ├─────────────────────┼─────────────────────────────────────────┼────────────────────────────┤
  │ Section heading     │ Heading                                 │ "Word on the Street"       │
  ├─────────────────────┼─────────────────────────────────────────┼────────────────────────────┤
  │ 3 Testimonial cards │ Testimonial widget or Text Editor cards │ Stars, quote, author, role │
  └─────────────────────┴─────────────────────────────────────────┴────────────────────────────┘

  Structure: 1 Section → Heading row → 3-column row

  Each card: star rating (Image or HTML), blockquote text, author initials + name, role label

  ---
  Section 11: Newsletter / Stay Connected

  Elementor Name: CTA – Newsletter Signup

  ┌────────────────┬─────────────────────┬──────────────────────────────────────┐
  │    Element     │       Widget        │                Notes                 │
  ├────────────────┼─────────────────────┼──────────────────────────────────────┤
  │ Heading        │ Heading             │ "Stay Connected — Get Event Updates" │
  ├────────────────┼─────────────────────┼──────────────────────────────────────┤
  │ Copy           │ Text Editor         │ Paragraph                            │
  ├────────────────┼─────────────────────┼──────────────────────────────────────┤
  │ Email form     │ Form widget         │ Email field + Subscribe button       │
  ├────────────────┼─────────────────────┼──────────────────────────────────────┤
  │ Disclaimer     │ Text Editor         │ "No spam." line                      │
  ├────────────────┼─────────────────────┼──────────────────────────────────────┤
  │ Social icons   │ Social Icons widget │ Instagram, Facebook, TikTok          │
  ├────────────────┼─────────────────────┼──────────────────────────────────────┤
  │ Hashtag prompt │ Text Editor         │ "@PartyLikeRico" tag line            │
  └────────────────┴─────────────────────┴──────────────────────────────────────┘

  Structure: 1 Section → 1–2 columns, centered content

  ---
  Section 12: Footer

  Elementor Name: Footer – Site Footer

  ┌────────────────┬──────────────────────────────┬───────────────────────────────┐
  │    Element     │            Widget            │             Notes             │
  ├────────────────┼──────────────────────────────┼───────────────────────────────┤
  │ Logo + tagline │ Image + Text Editor          │ Left column                   │
  ├────────────────┼──────────────────────────────┼───────────────────────────────┤
  │ Social icons   │ Social Icons                 │ Under logo                    │
  ├────────────────┼──────────────────────────────┼───────────────────────────────┤
  │ Events links   │ Nav Menu or Text Editor list │ Column 2                      │
  ├────────────────┼──────────────────────────────┼───────────────────────────────┤
  │ Company links  │ Nav Menu or Text Editor list │ Column 3                      │
  ├────────────────┼──────────────────────────────┼───────────────────────────────┤
  │ Contact info   │ Icon List                    │ Column 4 — phone, email, city │
  ├────────────────┼──────────────────────────────┼───────────────────────────────┤
  │ Tickets button │ Button                       │ Gold, full-width on mobile    │
  ├────────────────┼──────────────────────────────┼───────────────────────────────┤
  │ Copyright bar  │ Text Editor                  │ Bottom strip                  │
  └────────────────┴──────────────────────────────┴───────────────────────────────┘

  Structure: 1 Section → 4 columns → 1 full-width column below for copyright bar

  ---
  Global Style Notes for Elementor

  ┌─────────────────┬────────────────────────────────────────────────┐
  │    Property     │                     Value                      │
  ├─────────────────┼────────────────────────────────────────────────┤
  │ Primary color   │ #d4a017 (gold)                                 │
  ├─────────────────┼────────────────────────────────────────────────┤
  │ Accent/hover    │ #f0bf3a (bright gold)                          │
  ├─────────────────┼────────────────────────────────────────────────┤
  │ Background      │ #0a0a0a – #1a1a2e (dark)                       │
  ├─────────────────┼────────────────────────────────────────────────┤
  │ Text primary    │ #ffffff                                        │
  ├─────────────────┼────────────────────────────────────────────────┤
  │ Text secondary  │ #cccccc                                        │
  ├─────────────────┼────────────────────────────────────────────────┤
  │ Border style    │ 1px solid rgba(255,255,255,0.1)                │
  ├─────────────────┼────────────────────────────────────────────────┤
  │ Border radius   │ 8px–12px on cards                              │
  ├─────────────────┼────────────────────────────────────────────────┤
  │ Section padding │ 80px top/bottom desktop, 40px mobile           │
  ├─────────────────┼────────────────────────────────────────────────┤
  │ Font pairing    │ Display bold for headings, clean sans for body │
  └─────────────────┴────────────────────────────────────────────────┘

  ---
  Build Order Recommendation

  1. Set global colors + typography in Elementor Site Settings first
  2. Build Header template (display site-wide)
  3. Build Footer template (display site-wide)
  4. Build page sections top to bottom
  5. Use Elementor Inner Sections for all card layouts
  6. Use Loop Grid (Elementor Pro) if you want dynamic event cards later