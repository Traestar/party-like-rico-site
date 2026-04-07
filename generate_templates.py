#!/usr/bin/env python3
"""
Generate Elementor JSON page templates for Party Like Rico Promotions LLC.
Run: python generate_templates.py
"""

import json, random, string, os, zipfile

# ============================================================
# ID MANAGEMENT
# ============================================================
_used = set()

def uid():
    while True:
        x = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        if x not in _used:
            _used.add(x)
            return x

def reset_ids():
    _used.clear()

# ============================================================
# WIDGET BUILDERS
# ============================================================

def heading(title, size="h2", align="center", color="#FFFFFF", px=48,
            weight="900", transform="uppercase", family="Montserrat"):
    return {"id": uid(), "elType": "widget", "widgetType": "heading", "settings": {
        "title": title, "header_size": size, "align": align, "title_color": color,
        "typography_typography": "custom", "typography_font_family": family,
        "typography_font_size": {"unit": "px", "size": px},
        "typography_font_weight": weight, "typography_text_transform": transform,
    }}

def text_editor(content, color="#9CA3AF", px=18, align="center"):
    return {"id": uid(), "elType": "widget", "widgetType": "text-editor", "settings": {
        "editor": f'<p style="color:{color};font-size:{px}px;font-family:Inter,sans-serif;text-align:{align};line-height:1.7;margin:0;">{content}</p>'
    }}

def html_w(code):
    return {"id": uid(), "elType": "widget", "widgetType": "html", "settings": {"html": code}}

def spacer(h=20):
    return {"id": uid(), "elType": "widget", "widgetType": "spacer",
            "settings": {"space": {"unit": "px", "size": h}}}

# ============================================================
# LAYOUT BUILDERS
# ============================================================

def col(widgets, size=100, bg=None, pad=None):
    s = {"_column_size": size, "_inline_size": None}
    if bg: s["background_color"] = bg
    if pad: s["padding"] = pad
    return {"id": uid(), "elType": "column", "settings": s, "elements": widgets}

def sec(cols, bg="#0B0F14", pt="80", pb="80", pl="0", pr="0"):
    return {"id": uid(), "elType": "section", "settings": {
        "background_color": bg,
        "padding": {"unit": "px", "top": pt, "right": pr, "bottom": pb, "left": pl, "isLinked": False}
    }, "elements": cols}

# ============================================================
# COMMON COMPONENTS
# ============================================================

def label_html(text, color="#22C55E"):
    return (f'<div style="text-align:center;margin-bottom:16px;">'
            f'<span style="display:inline-block;background:{color}22;color:{color};'
            f'border:1px solid {color}55;padding:6px 20px;border-radius:50px;'
            f'font-family:Inter,sans-serif;font-size:11px;font-weight:700;'
            f'letter-spacing:2px;text-transform:uppercase;">{text}</span></div>')

def label_pill(text, color="#22C55E"):
    return html_w(label_html(text, color))

def page_struct(title, sections):
    return {
        "version": "0.4", "title": title, "type": "page",
        "page_settings": {"background_color": "#0B0F14", "hide_title": "yes"},
        "content": sections
    }

def hero_section(label, lc, h1, body, bg="#030b03"):
    return sec([col([spacer(20), label_pill(label, lc), spacer(8),
                     heading(h1, "h1", "center", "#FFFFFF", 80), spacer(16),
                     text_editor(body, "#9CA3AF", 18, "center"), spacer(20)])],
               bg=bg, pt="140", pb="80")

PAYPAL = "https://www.paypal.com/ncp/payment/AWCDNEHMYVWAG"

def link_btn(text, url, bg="#F97316", fg="#FFFFFF", outline=False, bc="rgba(255,255,255,0.3)"):
    if outline:
        return (f'<a href="{url}" style="display:inline-block;background:transparent;color:{fg};'
                f'text-decoration:none;padding:14px 32px;border-radius:50px;'
                f'border:2px solid {bc};font-family:Inter,sans-serif;font-size:14px;'
                f'font-weight:700;text-transform:uppercase;letter-spacing:1px;">{text}</a>')
    return (f'<a href="{url}" style="display:inline-block;background:{bg};color:{fg};'
            f'text-decoration:none;padding:14px 32px;border-radius:50px;'
            f'font-family:Inter,sans-serif;font-size:14px;font-weight:700;'
            f'text-transform:uppercase;letter-spacing:1px;">{text}</a>')

def btn_row(*btns):
    inner = "".join(btns)
    return html_w(f'<div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;">{inner}</div>')

# ============================================================
# PAGE 1: EVENTS PAGE
# ============================================================

def build_events():
    reset_ids()

    hero = hero_section("UPCOMING EXPERIENCES", "#22C55E", "EVENTS",
        "Browse all upcoming Party Like Rico events — bud crawls, nightlife, vendor pop-ups, "
        "shore experiences, and more. Atlantic City is waiting.")

    feat_html = f"""<div style="background:#0d1f0d;border:1px solid rgba(34,197,94,0.25);border-radius:16px;overflow:hidden;display:flex;flex-wrap:wrap;max-width:1100px;margin:0 auto;">
  <div style="flex:0 0 40%;min-width:280px;background:#091409;display:flex;align-items:center;justify-content:center;min-height:340px;flex-direction:column;">
    <div style="font-size:80px;margin-bottom:12px;">🌿</div>
    <p style="color:#22C55E;font-family:Montserrat,sans-serif;font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin:0;">Event Flyer</p>
  </div>
  <div style="flex:1;padding:48px 40px;min-width:280px;">
    <span style="display:inline-block;background:#22C55E22;color:#22C55E;border:1px solid #22C55E55;padding:5px 16px;border-radius:50px;font-family:Inter,sans-serif;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:20px;">🌿 FEATURED EVENT 2026</span>
    <h2 style="font-family:Montserrat,sans-serif;font-weight:900;text-transform:uppercase;color:#fff;font-size:36px;line-height:1.15;margin:0 0 16px;">420 WEEKEND AC <span style="color:#FACC15;">BUD CRAWL</span></h2>
    <div style="display:flex;flex-wrap:wrap;gap:16px;margin-bottom:12px;">
      <span style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:14px;">📅 <strong style="color:#FACC15;">Saturday, April 18, 2026</strong></span>
      <span style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:14px;">🕐 1PM – 7PM</span>
      <span style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:14px;">🔞 21+ Only</span>
    </div>
    <div style="display:flex;flex-wrap:wrap;gap:16px;margin-bottom:20px;">
      <span style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:14px;">📍 Atlantic City, NJ</span>
      <span style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:14px;">💵 $25 Entry</span>
    </div>
    <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:14px;line-height:1.7;margin:0 0 28px;">Join Atlantic City's premiere 420 experience — a curated bud crawl through AC's hottest venues. Live music, curated stops, and unforgettable vibes.</p>
    <div style="display:flex;gap:12px;flex-wrap:wrap;">
      <a href="{PAYPAL}" style="display:inline-block;background:#F97316;color:#fff;text-decoration:none;padding:14px 28px;border-radius:50px;font-family:Inter,sans-serif;font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:1px;">🎟 Buy Tickets Now</a>
      <a href="/events/bud-crawl" style="display:inline-block;background:transparent;color:#fff;text-decoration:none;padding:14px 28px;border-radius:50px;border:2px solid rgba(255,255,255,0.25);font-family:Inter,sans-serif;font-size:13px;font-weight:700;text-transform:uppercase;letter-spacing:1px;">View Details</a>
    </div>
  </div>
</div>"""
    feat_sec = sec([col([html_w(feat_html)])], bg="#121826", pt="60", pb="60")

    filter_html = """<div style="display:flex;flex-wrap:wrap;gap:10px;justify-content:center;padding:4px 20px;">
  <button style="background:rgba(250,204,21,0.15);color:#FACC15;border:1.5px solid rgba(250,204,21,0.4);padding:8px 22px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1px;cursor:pointer;">All Events</button>
  <button style="background:transparent;color:#9CA3AF;border:1.5px solid rgba(255,255,255,0.1);padding:8px 22px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1px;cursor:pointer;">Featured</button>
  <button style="background:transparent;color:#9CA3AF;border:1.5px solid rgba(255,255,255,0.1);padding:8px 22px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1px;cursor:pointer;">Bud Crawls</button>
  <button style="background:transparent;color:#9CA3AF;border:1.5px solid rgba(255,255,255,0.1);padding:8px 22px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1px;cursor:pointer;">Nightlife</button>
  <button style="background:transparent;color:#9CA3AF;border:1.5px solid rgba(255,255,255,0.1);padding:8px 22px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1px;cursor:pointer;">Community</button>
  <button style="background:transparent;color:#9CA3AF;border:1.5px solid rgba(255,255,255,0.1);padding:8px 22px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1px;cursor:pointer;">Vendor Pop-Up</button>
  <button style="background:transparent;color:#9CA3AF;border:1.5px solid rgba(255,255,255,0.1);padding:8px 22px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1px;cursor:pointer;">Private</button>
</div>"""
    filter_sec = sec([col([html_w(filter_html)])], bg="#0B0F14", pt="24", pb="24")

    def ev_card(badge, bc, date, title, desc, btn_txt, btn_url, outline=False, emoji="🎉"):
        bstyle = "background:#F97316;color:#fff;" if not outline else "background:transparent;color:#fff;border:2px solid rgba(255,255,255,0.3);"
        return html_w(f"""<div style="background:#0e1218;border:1px solid rgba(255,255,255,0.06);border-radius:14px;overflow:hidden;transition:all 0.3s ease;height:100%;" onmouseover="this.style.transform='translateY(-6px)';this.style.boxShadow='0 20px 50px rgba(0,0,0,0.5)';" onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='none';">
  <div style="position:relative;aspect-ratio:16/10;background:#111;display:flex;align-items:center;justify-content:center;">
    <span style="font-size:52px;">{emoji}</span>
    <span style="position:absolute;top:12px;left:12px;background:{bc}22;color:{bc};border:1px solid {bc}55;padding:4px 12px;border-radius:50px;font-family:Inter,sans-serif;font-size:11px;font-weight:700;text-transform:uppercase;">{badge}</span>
  </div>
  <div style="padding:20px;">
    <p style="color:#FACC15;font-family:Inter,sans-serif;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:2px;margin:0 0 8px;">{date}</p>
    <h4 style="color:#fff;font-family:Montserrat,sans-serif;font-weight:700;font-size:16px;text-transform:uppercase;margin:0 0 8px;line-height:1.3;">{title}</h4>
    <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:13px;line-height:1.6;margin:0 0 16px;">{desc}</p>
    <div style="display:flex;align-items:center;justify-content:space-between;padding-top:12px;border-top:1px solid rgba(255,255,255,0.06);">
      <span style="color:#9CA3AF;font-size:12px;font-family:Inter,sans-serif;">📍 Atlantic City, NJ</span>
      <a href="{btn_url}" style="display:inline-block;{bstyle}text-decoration:none;padding:8px 18px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;text-transform:uppercase;">{btn_txt}</a>
    </div>
  </div>
</div>""")

    grid_r1 = sec([
        col([ev_card("🌿 Featured", "#22C55E", "SAT · APRIL 18 2026", "420 Weekend AC Bud Crawl",
                     "Atlantic City's premiere 420 experience — curated stops, live music, and unforgettable vibes.",
                     "Buy Tickets", PAYPAL, False, "🌿")], 33),
        col([ev_card("Nightlife", "#A855F7", "MAY 2026 · TBD", "Summer Kickoff AC",
                     "Kick off the summer with AC's hottest nightlife event. Details dropping soon.",
                     "Details →", "#", True, "🎆")], 33),
        col([ev_card("Vendor Market", "#3B82F6", "JUNE 2026 · TBD", "Summer Vendor Pop-Up Market",
                     "Local vendors, artists, and brands come together for a premier pop-up market experience.",
                     "Details →", "#", True, "🏪")], 33),
    ], bg="#0B0F14", pt="60", pb="20")

    grid_r2 = sec([
        col([ev_card("Holiday", "#FACC15", "JULY 4, 2026", "Independence Day AC",
                     "Celebrate Independence Day Atlantic City style — fireworks, music, and Jersey Shore energy.",
                     "Details →", "#", True, "🎇")], 33),
        col([ev_card("Shore Event", "#06B6D4", "AUGUST 2026 · TBD", "End of Summer Shore Bash",
                     "Send off the summer with the biggest shore bash in Atlantic City. Stay tuned for details.",
                     "Details →", "#", True, "🏖")], 33),
        col([ev_card("Community", "#EC4899", "SEPT 2026 · TBD", "AC Community Celebration",
                     "A celebration of the Atlantic City community — art, culture, music, and togetherness.",
                     "Details →", "#", True, "🎊")], 33),
    ], bg="#0B0F14", pt="20", pb="60")

    promote_sec = sec([col([
        label_pill("PARTNER WITH US", "#FACC15"), spacer(8),
        heading("WANT YOUR EVENT LISTED?", "h2", "center", "#FFFFFF", 48), spacer(16),
        text_editor("We work with local businesses, artists, promoters, and brands across Atlantic City. "
                    "Let&#8217;s put your event in front of the right audience.", "#9CA3AF", 16, "center"),
        spacer(24),
        btn_row(link_btn("Learn How We Promote", "/promote", "#FACC15", "#0B0F14"),
                link_btn("Contact Us", "/contact", outline=True)),
    ])], bg="#121826", pt="80", pb="80")

    return page_struct("Events | Party Like Rico",
                       [hero, feat_sec, filter_sec, grid_r1, grid_r2, promote_sec])


# ============================================================
# PAGE 2: MEDIA PAGE
# ============================================================

def build_media():
    reset_ids()

    hero = hero_section("PHOTOS · FLYERS · RECAPS", "#22C55E", "MEDIA &amp; GALLERY",
        "Relive the moments that made the night unforgettable. Browse event photos, flyers, "
        "recaps, and highlights from Party Like Rico events.")

    flyer_html = f"""<div style="display:flex;flex-wrap:wrap;gap:40px;max-width:1000px;margin:0 auto;align-items:center;">
  <div style="flex:0 0 280px;">
    <div style="aspect-ratio:3/4;background:#1A2233;border-radius:12px;display:flex;align-items:center;justify-content:center;box-shadow:0 30px 80px rgba(0,0,0,0.6);border:1px solid rgba(34,197,94,0.2);">
      <div style="text-align:center;"><div style="font-size:80px;margin-bottom:12px;">🌿</div><p style="color:#22C55E;font-family:Montserrat,sans-serif;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin:0;">Official Flyer</p></div>
    </div>
  </div>
  <div style="flex:1;min-width:260px;">
    {label_html("FEATURED", "#FACC15")}
    <h2 style="font-family:Montserrat,sans-serif;font-weight:900;text-transform:uppercase;color:#fff;font-size:36px;line-height:1.15;margin:0 0 20px;">OFFICIAL EVENT <span style="color:#FACC15;">FLYER</span></h2>
    <div style="display:flex;flex-direction:column;gap:10px;margin-bottom:24px;">
      <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:14px;margin:0;"><strong style="color:#FACC15;">📅 Date:</strong> Saturday, April 18, 2026</p>
      <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:14px;margin:0;"><strong style="color:#FACC15;">🕐 Time:</strong> 1PM – 7PM</p>
      <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:14px;margin:0;"><strong style="color:#FACC15;">📍 Location:</strong> Atlantic City, NJ</p>
      <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:14px;margin:0;"><strong style="color:#FACC15;">🔞 Age:</strong> 21+ Only</p>
      <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:14px;margin:0;"><strong style="color:#FACC15;">💵 Price:</strong> $25 Entry</p>
    </div>
    <div style="display:flex;gap:12px;flex-wrap:wrap;">
      <a href="{PAYPAL}" style="display:inline-block;background:#F97316;color:#fff;text-decoration:none;padding:14px 28px;border-radius:50px;font-family:Inter,sans-serif;font-size:13px;font-weight:700;text-transform:uppercase;">🎟 Buy Tickets — $25</a>
      <a href="/events" style="display:inline-block;background:transparent;color:#fff;text-decoration:none;padding:14px 28px;border-radius:50px;border:2px solid rgba(255,255,255,0.25);font-family:Inter,sans-serif;font-size:13px;font-weight:700;text-transform:uppercase;">View Events</a>
    </div>
  </div>
</div>"""
    flyer_sec = sec([col([html_w(flyer_html)])], bg="#030b03", pt="80", pb="80")

    gallery_filter = """<div style="display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin-bottom:32px;">
  <button style="background:rgba(250,204,21,0.15);color:#FACC15;border:1.5px solid rgba(250,204,21,0.4);padding:8px 22px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1px;cursor:pointer;">All</button>
  <button style="background:transparent;color:#9CA3AF;border:1.5px solid rgba(255,255,255,0.1);padding:8px 22px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1px;cursor:pointer;">Bud Crawl</button>
  <button style="background:transparent;color:#9CA3AF;border:1.5px solid rgba(255,255,255,0.1);padding:8px 22px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1px;cursor:pointer;">Nightlife</button>
  <button style="background:transparent;color:#9CA3AF;border:1.5px solid rgba(255,255,255,0.1);padding:8px 22px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1px;cursor:pointer;">Vendors</button>
  <button style="background:transparent;color:#9CA3AF;border:1.5px solid rgba(255,255,255,0.1);padding:8px 22px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1px;cursor:pointer;">Community</button>
</div>"""
    gallery_cells = ""
    for e in ["🌿", "🎉", "🎶", "🌃", "🍻", "🎤", "🎊", "🏙", "🌟"]:
        gallery_cells += (f'<div style="aspect-ratio:1;background:#111;border-radius:8px;'
                          f'display:flex;align-items:center;justify-content:center;overflow:hidden;'
                          f'position:relative;cursor:pointer;" '
                          f'onmouseover="this.children[1].style.opacity=\'1\';" '
                          f'onmouseout="this.children[1].style.opacity=\'0\';">'
                          f'<span style="font-size:36px;">{e}</span>'
                          f'<div style="position:absolute;inset:0;background:rgba(0,0,0,0.75);'
                          f'display:flex;align-items:center;justify-content:center;opacity:0;'
                          f'transition:opacity 0.3s ease;font-size:28px;">🔍</div></div>')
    gallery_html = (f'{gallery_filter}'
                    f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:12px;">'
                    f'{gallery_cells}</div>')
    gallery_sec = sec([col([
        label_pill("GALLERY", "#FACC15"), spacer(8),
        heading('EVENT <span style="color:#FACC15;">PHOTOS</span>', "h2", "center", "#FFFFFF", 48),
        spacer(32), html_w(gallery_html),
    ])], bg="#0B0F14", pt="80", pb="80")

    def recap_card(icon, badge, bc, title, desc):
        return html_w(f"""<div style="background:#1A2233;border:1px solid rgba(255,255,255,0.07);border-radius:14px;overflow:hidden;height:100%;transition:all 0.3s ease;" onmouseover="this.style.transform='translateY(-4px)';this.style.boxShadow='0 16px 40px rgba(0,0,0,0.4)';" onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='none';">
  <div style="position:relative;aspect-ratio:16/9;background:#0e1218;display:flex;align-items:center;justify-content:center;">
    <span style="font-size:48px;">{icon}</span>
    <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(0,0,0,0.3);"><span style="font-size:36px;background:rgba(0,0,0,0.6);border-radius:50%;width:60px;height:60px;display:flex;align-items:center;justify-content:center;">▶️</span></div>
  </div>
  <div style="padding:20px;">
    <span style="display:inline-block;background:{bc}22;color:{bc};border:1px solid {bc}55;padding:3px 10px;border-radius:50px;font-family:Inter,sans-serif;font-size:11px;font-weight:700;text-transform:uppercase;margin-bottom:12px;">{badge}</span>
    <h4 style="color:#fff;font-family:Montserrat,sans-serif;font-weight:700;font-size:15px;text-transform:uppercase;margin:0 0 8px;line-height:1.3;">{title}</h4>
    <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:13px;line-height:1.6;margin:0;">{desc}</p>
  </div>
</div>""")

    recaps_header = sec([col([
        label_pill("RECAPS", "#FACC15"), spacer(8),
        heading('EVENT <span style="color:#FACC15;">HIGHLIGHTS</span>', "h2", "center", "#FFFFFF", 48),
        spacer(16),
    ])], bg="#121826", pt="60", pb="0")
    recaps_sec = sec([
        col([recap_card("🌿", "Event Recap", "#22C55E",
                        "420 Weekend AC Bud Crawl — Coming April 2026",
                        "The full event recap drops after April 18th. Check back for photos, highlights, and behind-the-scenes content.")], 33),
        col([recap_card("📱", "Summer Preview", "#F97316",
                        "Summer 2026 Event Series — First Look",
                        "Get an early look at what's coming this summer — new venues, new events, and all new energy across Atlantic City.")], 33),
        col([recap_card("🎤", "Behind the Brand", "#A855F7",
                        "Behind the Brand — Rico's Vision for AC",
                        "An exclusive look into what drives Party Like Rico Promotions and the mission to make Atlantic City unforgettable.")], 33),
    ], bg="#121826", pt="0", pb="80")

    social_cta_sec = sec([col([
        label_pill("SOCIAL", "#22C55E"), spacer(8),
        heading('FOLLOW THE <span style="color:#FACC15;">VIBE</span>', "h2", "center", "#FFFFFF", 48),
        spacer(16),
        text_editor("Follow @PartyLikeRico for daily updates, behind-the-scenes content, and event announcements.", "#9CA3AF", 16, "center"),
        spacer(24),
        btn_row(link_btn("Instagram", "#instagram", "#FACC15", "#0B0F14"),
                link_btn("Facebook", "#facebook", outline=True),
                link_btn("TikTok", "#tiktok", outline=True)),
    ])], bg="#060a06", pt="80", pb="80")

    social_cells = ""
    for e in ["🌿", "🎉", "🌃", "🎶", "🏙", "🎊", "🌟", "🎤"]:
        social_cells += (f'<div style="aspect-ratio:1;background:#0e1218;border-radius:10px;'
                         f'display:flex;align-items:center;justify-content:center;overflow:hidden;'
                         f'position:relative;cursor:pointer;" '
                         f'onmouseover="this.children[1].style.opacity=\'1\';" '
                         f'onmouseout="this.children[1].style.opacity=\'0\';">'
                         f'<span style="font-size:32px;">{e}</span>'
                         f'<div style="position:absolute;inset:0;background:rgba(0,0,0,0.75);'
                         f'display:flex;align-items:center;justify-content:center;opacity:0;'
                         f'transition:opacity 0.3s ease;font-size:24px;">📲</div></div>')
    social_grid_html = (f'<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-bottom:20px;">'
                        f'{social_cells}</div>'
                        f'<p style="text-align:center;color:#9CA3AF;font-family:Inter,sans-serif;font-size:13px;margin:0;">'
                        f'Tag us at <strong style="color:#FACC15;">@PartyLikeRico</strong> to be featured here</p>')
    social_grid_sec = sec([col([
        label_pill("SOCIAL HIGHLIGHTS", "#FACC15"), spacer(8),
        heading('TAG <span style="color:#FACC15;">@PARTYLIKERICO</span>', "h2", "center", "#FFFFFF", 48),
        spacer(32), html_w(social_grid_html),
    ])], bg="#0B0F14", pt="80", pb="80")

    return page_struct("Media & Gallery | Party Like Rico",
                       [hero, flyer_sec, gallery_sec, recaps_header, recaps_sec,
                        social_cta_sec, social_grid_sec])


# ============================================================
# PAGE 3: PROMOTE PAGE
# ============================================================

def build_promote():
    reset_ids()

    hero = hero_section("GROW YOUR BRAND", "#F97316", "PROMOTE WITH RICO",
        "Partner with Party Like Rico Promotions and put your brand in front of "
        "Atlantic City's most engaged audience.")

    def svc_card(icon, title, body):
        return html_w(f"""<div style="background:#1A2233;border:1px solid rgba(255,255,255,0.07);border-radius:14px;padding:28px;height:100%;transition:all 0.3s ease;" onmouseover="this.style.transform='translateY(-4px)';this.style.borderColor='rgba(249,115,22,0.3)';" onmouseout="this.style.transform='translateY(0)';this.style.borderColor='rgba(255,255,255,0.07)';">
  <div style="font-size:36px;margin-bottom:16px;">{icon}</div>
  <h4 style="color:#fff;font-family:Montserrat,sans-serif;font-weight:700;font-size:16px;text-transform:uppercase;margin:0 0 10px;">{title}</h4>
  <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:13px;line-height:1.7;margin:0;">{body}</p>
</div>""")

    svc_header = sec([col([
        label_pill("OUR SERVICES", "#F97316"), spacer(8),
        heading('WHAT WE <span style="color:#FACC15;">OFFER</span>', "h2", "center", "#FFFFFF", 48),
        spacer(8),
        text_editor("From event promotion to full coordination — we handle it all.", "#9CA3AF", 16, "center"),
        spacer(32),
    ])], bg="#0B0F14", pt="80", pb="0")
    svc_r1 = sec([
        col([svc_card("📣", "Event Promotion", "We promote your event across our full social, email, and on-the-ground network.")], 33),
        col([svc_card("🎨", "Flyer &amp; Brand Design", "Eye-catching event flyers and marketing materials that cut through the noise.")], 33),
        col([svc_card("🚌", "Shuttle Party Coordination", "Full shuttle party logistics — venues, transportation, timeline, execution.")], 33),
    ], bg="#0B0F14", pt="0", pb="20")
    svc_r2 = sec([
        col([svc_card("📱", "Social Media Coverage", "Live coverage, stories, reels, and post-event recap content for your brand.")], 33),
        col([svc_card("🤝", "Vendor Placement", "We place your brand or product at the right events in front of the right audience.")], 33),
        col([svc_card("🎤", "Private Event Planning", "Birthdays, bachelorettes, corporate events — we handle it all end to end.")], 33),
    ], bg="#0B0F14", pt="20", pb="80")

    def step_card(num, icon, title, body):
        return html_w(f"""<div style="background:#1A2233;border:1px solid rgba(255,255,255,0.07);border-radius:14px;padding:32px 24px;text-align:center;height:100%;position:relative;overflow:hidden;">
  <div style="position:absolute;top:-10px;right:16px;font-family:Montserrat,sans-serif;font-weight:900;font-size:80px;color:rgba(255,255,255,0.04);line-height:1;user-select:none;">{num}</div>
  <div style="font-size:40px;margin-bottom:16px;">{icon}</div>
  <div style="display:inline-block;background:rgba(250,204,21,0.1);color:#FACC15;border:1px solid rgba(250,204,21,0.3);padding:3px 12px;border-radius:50px;font-family:Inter,sans-serif;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin-bottom:12px;">Step {num}</div>
  <h4 style="color:#fff;font-family:Montserrat,sans-serif;font-weight:700;font-size:16px;text-transform:uppercase;margin:0 0 10px;">{title}</h4>
  <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:13px;line-height:1.7;margin:0;">{body}</p>
</div>""")

    hiw_header = sec([col([
        label_pill("PROCESS", "#FACC15"), spacer(8),
        heading('HOW IT <span style="color:#FACC15;">WORKS</span>', "h2", "center", "#FFFFFF", 48),
        spacer(32),
    ])], bg="#121826", pt="80", pb="0")
    hiw_steps = sec([
        col([step_card("1", "🙋", "Reach Out", "Contact us via the form or phone. Tell us about your event or brand.")], 25),
        col([step_card("2", "📋", "We Plan", "We build a custom promotion strategy tailored to your goals.")], 25),
        col([step_card("3", "📣", "We Execute", "We launch across all channels — social, email, and on the ground.")], 25),
        col([step_card("4", "🎉", "You Shine", "Your event is packed, your brand is seen, your audience grows.")], 25),
    ], bg="#121826", pt="0", pb="80")

    who_html = """<div style="background:#1A2233;border:1px solid rgba(255,255,255,0.07);border-radius:16px;padding:40px;height:100%;">
  <h3 style="color:#fff;font-family:Montserrat,sans-serif;font-weight:900;font-size:24px;text-transform:uppercase;margin:0 0 24px;">Who We Help</h3>
  <div style="display:flex;flex-direction:column;gap:14px;">
    <div style="display:flex;align-items:center;gap:12px;"><span style="color:#22C55E;font-size:18px;">✅</span><span style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:14px;">Cannabis brands &amp; dispensaries</span></div>
    <div style="display:flex;align-items:center;gap:12px;"><span style="color:#22C55E;font-size:18px;">✅</span><span style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:14px;">Local Atlantic City businesses</span></div>
    <div style="display:flex;align-items:center;gap:12px;"><span style="color:#22C55E;font-size:18px;">✅</span><span style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:14px;">Artists &amp; DJs</span></div>
    <div style="display:flex;align-items:center;gap:12px;"><span style="color:#22C55E;font-size:18px;">✅</span><span style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:14px;">Bars &amp; nightclubs</span></div>
    <div style="display:flex;align-items:center;gap:12px;"><span style="color:#22C55E;font-size:18px;">✅</span><span style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:14px;">Vendors &amp; pop-up sellers</span></div>
    <div style="display:flex;align-items:center;gap:12px;"><span style="color:#22C55E;font-size:18px;">✅</span><span style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:14px;">Corporate event organizers</span></div>
  </div>
</div>"""
    cta_right_html = f"""<div style="background:#1A2233;border:2px solid #FACC15;border-radius:16px;padding:40px;text-align:center;height:100%;">
  <h3 style="color:#fff;font-family:Montserrat,sans-serif;font-weight:900;font-size:28px;text-transform:uppercase;margin:0 0 16px;">Ready to <span style="color:#FACC15;">Promote?</span></h3>
  <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:14px;line-height:1.7;margin:0 0 24px;">Tell us about your brand, event, or idea. We'll build a custom strategy to get you in front of Atlantic City's most engaged audience.</p>
  <a href="/contact" style="display:inline-block;background:#F97316;color:#fff;text-decoration:none;padding:14px 32px;border-radius:50px;font-family:Inter,sans-serif;font-size:14px;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin-bottom:20px;">Get In Touch</a>
  <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:13px;margin:8px 0 0;">📞 <a href="tel:6095942265" style="color:#FACC15;text-decoration:none;font-weight:700;">(609) 594-2265</a></p>
</div>"""
    who_cta_sec = sec([col([html_w(who_html)], 60), col([html_w(cta_right_html)], 40)],
                      bg="#0B0F14", pt="80", pb="80")

    final_sec = sec([col([
        label_pill("PARTNER WITH US", "#F97316"), spacer(8),
        heading("READY TO GROW?", "h2", "center", "#FFFFFF", 48), spacer(16),
        text_editor("Put your brand where the party is. Let&#8217;s build something great together.", "#9CA3AF", 16, "center"),
        spacer(24),
        btn_row(link_btn("Become a Vendor", "/vendor"),
                link_btn("Contact Us", "/contact", outline=True)),
    ])], bg="#060a06", pt="80", pb="80")

    return page_struct("Promote With Rico | Party Like Rico",
                       [hero, svc_header, svc_r1, svc_r2, hiw_header, hiw_steps, who_cta_sec, final_sec])


# ============================================================
# PAGE 4: CONTACT PAGE
# ============================================================

def build_contact():
    reset_ids()

    hero = hero_section("REACH OUT", "#F97316", "CONTACT US",
        "Questions about an event, ticket help, vendor inquiries, partnerships, or a private celebration? "
        "We&#8217;d love to hear from you.")

    left_html = f"""<div style="display:flex;flex-direction:column;gap:24px;">
  <div style="background:#1A2233;border:1px solid rgba(255,255,255,0.07);border-radius:16px;padding:40px;">
    <h3 style="color:#fff;font-family:Montserrat,sans-serif;font-weight:900;font-size:24px;text-transform:uppercase;margin:0 0 8px;">Send a Message</h3>
    <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:14px;line-height:1.7;margin:0 0 24px;">Fill out the form below and we'll get back to you within 24–48 hours.</p>
    <div style="border:2px dashed rgba(255,255,255,0.15);border-radius:10px;padding:32px;text-align:center;">
      <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:13px;line-height:1.7;margin:0 0 8px;">Insert WPForms Contact Form shortcode here:</p>
      <code style="color:#FACC15;font-family:monospace;font-size:14px;background:rgba(250,204,21,0.1);padding:6px 12px;border-radius:6px;">[wpforms id="contact-form-id"]</code>
    </div>
  </div>
  <div style="background:#1A2233;border:2px solid #FACC15;border-radius:16px;padding:32px;">
    <div style="font-size:32px;margin-bottom:12px;">🤝</div>
    <h4 style="color:#fff;font-family:Montserrat,sans-serif;font-weight:700;font-size:18px;text-transform:uppercase;margin:0 0 10px;">Vendor &amp; Partnership Inquiries</h4>
    <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:13px;line-height:1.7;margin:0 0 16px;">Interested in vending at a Party Like Rico event? Want to partner with us for promotion or sponsorship? We'd love to connect.</p>
    <a href="/vendor" style="display:inline-block;background:#FACC15;color:#0B0F14;text-decoration:none;padding:12px 24px;border-radius:50px;font-family:Inter,sans-serif;font-size:13px;font-weight:700;text-transform:uppercase;">Vendor Application →</a>
  </div>
</div>"""

    right_html = f"""<div style="background:#1A2233;border:1px solid rgba(255,255,255,0.07);border-radius:16px;padding:40px;height:100%;">
  <h3 style="color:#fff;font-family:Montserrat,sans-serif;font-weight:900;font-size:24px;text-transform:uppercase;margin:0 0 24px;">Get In Touch</h3>
  <div style="display:flex;flex-direction:column;gap:20px;margin-bottom:28px;">
    <div style="display:flex;align-items:flex-start;gap:16px;"><span style="font-size:22px;min-width:32px;">📞</span><div><p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin:0 0 4px;">Phone</p><a href="tel:6095942265" style="color:#FFFFFF;font-family:Inter,sans-serif;font-size:15px;font-weight:600;text-decoration:none;">(609) 594-2265</a></div></div>
    <div style="display:flex;align-items:flex-start;gap:16px;"><span style="font-size:22px;min-width:32px;">✉️</span><div><p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin:0 0 4px;">Email</p><a href="mailto:PartyLikeRico@gmail.com" style="color:#FFFFFF;font-family:Inter,sans-serif;font-size:15px;font-weight:600;text-decoration:none;">PartyLikeRico@gmail.com</a></div></div>
    <div style="display:flex;align-items:flex-start;gap:16px;"><span style="font-size:22px;min-width:32px;">📍</span><div><p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin:0 0 4px;">Location</p><p style="color:#FFFFFF;font-family:Inter,sans-serif;font-size:15px;font-weight:600;margin:0;">Atlantic City, NJ</p></div></div>
    <div style="display:flex;align-items:flex-start;gap:16px;"><span style="font-size:22px;min-width:32px;">🌐</span><div><p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin:0 0 4px;">Website</p><a href="https://acbudcrawl.com" style="color:#FACC15;font-family:Inter,sans-serif;font-size:15px;font-weight:600;text-decoration:none;">acbudcrawl.com</a></div></div>
  </div>
  <div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:24px;">
    <a href="#ig" style="background:#0B0F14;border:1px solid rgba(255,255,255,0.15);color:#9CA3AF;text-decoration:none;padding:8px 16px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;">IG</a>
    <a href="#fb" style="background:#0B0F14;border:1px solid rgba(255,255,255,0.15);color:#9CA3AF;text-decoration:none;padding:8px 16px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;">FB</a>
    <a href="#tt" style="background:#0B0F14;border:1px solid rgba(255,255,255,0.15);color:#9CA3AF;text-decoration:none;padding:8px 16px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;">TT</a>
    <a href="#x" style="background:#0B0F14;border:1px solid rgba(255,255,255,0.15);color:#9CA3AF;text-decoration:none;padding:8px 16px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;">X</a>
  </div>
  <div style="background:#0B0F14;border:2px solid #22C55E;border-radius:12px;padding:20px;">
    <span style="display:inline-block;background:#22C55E22;color:#22C55E;border:1px solid #22C55E55;padding:3px 10px;border-radius:50px;font-family:Inter,sans-serif;font-size:11px;font-weight:700;text-transform:uppercase;margin-bottom:12px;">🌿 Upcoming Event</span>
    <h4 style="color:#fff;font-family:Montserrat,sans-serif;font-weight:700;font-size:15px;text-transform:uppercase;margin:0 0 6px;">420 Weekend AC Bud Crawl</h4>
    <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:13px;margin:0 0 4px;">📅 April 18, 2026 · 1PM–7PM</p>
    <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:13px;margin:0 0 16px;">💵 $25 Entry · 21+</p>
    <a href="{PAYPAL}" style="display:inline-block;background:#F97316;color:#fff;text-decoration:none;padding:10px 20px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;text-transform:uppercase;">🎟 Buy Tickets</a>
  </div>
</div>"""

    contact_layout = sec([col([html_w(left_html)], 60), col([html_w(right_html)], 40)],
                         bg="#0B0F14", pt="80", pb="80")

    quick_html = """<div style="display:flex;flex-wrap:wrap;gap:20px;justify-content:center;">
  <a href="tel:6095942265" style="display:flex;align-items:center;gap:12px;background:#1A2233;border:1px solid rgba(255,255,255,0.07);text-decoration:none;padding:20px 32px;border-radius:50px;min-width:220px;justify-content:center;transition:all 0.3s ease;" onmouseover="this.style.borderColor='rgba(249,115,22,0.4)';" onmouseout="this.style.borderColor='rgba(255,255,255,0.07)';">
    <span style="font-size:24px;">📞</span>
    <div><p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin:0 0 2px;">Phone</p><p style="color:#fff;font-family:Inter,sans-serif;font-size:15px;font-weight:600;margin:0;">(609) 594-2265</p></div>
  </a>
  <a href="mailto:PartyLikeRico@gmail.com" style="display:flex;align-items:center;gap:12px;background:#1A2233;border:1px solid rgba(255,255,255,0.07);text-decoration:none;padding:20px 32px;border-radius:50px;min-width:220px;justify-content:center;transition:all 0.3s ease;" onmouseover="this.style.borderColor='rgba(250,204,21,0.4)';" onmouseout="this.style.borderColor='rgba(255,255,255,0.07)';">
    <span style="font-size:24px;">✉️</span>
    <div><p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin:0 0 2px;">Email</p><p style="color:#fff;font-family:Inter,sans-serif;font-size:15px;font-weight:600;margin:0;">PartyLikeRico@gmail.com</p></div>
  </a>
  <a href="sms:6095942265" style="display:flex;align-items:center;gap:12px;background:#22C55E;border:1px solid #22C55E;text-decoration:none;padding:20px 32px;border-radius:50px;min-width:220px;justify-content:center;" onmouseover="this.style.opacity='0.9';" onmouseout="this.style.opacity='1';">
    <span style="font-size:24px;">💬</span>
    <div><p style="color:rgba(255,255,255,0.8);font-family:Inter,sans-serif;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin:0 0 2px;">Text Us</p><p style="color:#fff;font-family:Inter,sans-serif;font-size:15px;font-weight:600;margin:0;">(609) 594-2265</p></div>
  </a>
</div>"""
    quick_sec = sec([col([
        label_pill("DIRECT CONTACT", "#F97316"), spacer(8),
        heading("REACH US DIRECTLY", "h2", "center", "#FFFFFF", 48),
        spacer(32), html_w(quick_html),
    ])], bg="#121826", pt="80", pb="80")

    return page_struct("Contact Us | Party Like Rico", [hero, contact_layout, quick_sec])


# ============================================================
# PAGE 5: ABOUT PAGE
# ============================================================

def build_about():
    reset_ids()

    hero = hero_section("OUR STORY", "#FACC15", "ABOUT PARTY LIKE RICO",
        "We're Atlantic City's event promotion company — built to connect people with unforgettable "
        "experiences and the energy that makes the Jersey Shore unlike anywhere else.")

    left_img_html = """<div style="position:relative;display:inline-block;width:100%;">
  <div style="aspect-ratio:4/5;background:#1A2233;border-radius:16px;display:flex;align-items:center;justify-content:center;overflow:hidden;">
    <span style="font-size:100px;">🏙</span>
  </div>
  <div style="position:absolute;bottom:-16px;left:-16px;background:#1A2233;border:2px solid #FACC15;border-radius:12px;padding:16px 24px;box-shadow:0 8px 32px rgba(0,0,0,0.5);">
    <p style="color:#FACC15;font-family:Montserrat,sans-serif;font-weight:900;font-size:36px;margin:0;line-height:1;">2026</p>
    <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin:0;">Year Founded</p>
  </div>
</div>"""
    right_intro_html = f"""<div style="padding:20px 0 20px 20px;">
  <span style="display:inline-block;background:#22C55E22;color:#22C55E;border:1px solid #22C55E55;padding:5px 16px;border-radius:50px;font-family:Inter,sans-serif;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:20px;">WHO WE ARE</span>
  <h2 style="font-family:Montserrat,sans-serif;font-weight:900;text-transform:uppercase;color:#fff;font-size:36px;line-height:1.2;margin:0 0 20px;">MORE THAN AN EVENT COMPANY — WE CREATE <span style="color:#FACC15;">MOMENTS</span></h2>
  <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:15px;line-height:1.8;margin:0 0 16px;">Party Like Rico Promotions LLC was born from a passion for Atlantic City's nightlife, culture, and community. We believe every event should be more than a night out — it should be a memory.</p>
  <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:15px;line-height:1.8;margin:0 0 28px;">From curated bud crawls and shore experiences to private events and brand activations — we bring the vision, the network, and the execution to make it happen.</p>
  <div style="display:flex;gap:12px;flex-wrap:wrap;">
    <a href="/events" style="display:inline-block;background:#F97316;color:#fff;text-decoration:none;padding:14px 28px;border-radius:50px;font-family:Inter,sans-serif;font-size:13px;font-weight:700;text-transform:uppercase;">See Our Events</a>
    <a href="/about#mission" style="display:inline-block;background:transparent;color:#fff;text-decoration:none;padding:14px 28px;border-radius:50px;border:2px solid rgba(255,255,255,0.25);font-family:Inter,sans-serif;font-size:13px;font-weight:700;text-transform:uppercase;">Our Mission</a>
  </div>
</div>"""
    intro_sec = sec([col([html_w(left_img_html)], 45), col([html_w(right_intro_html)], 55)],
                    bg="#0B0F14", pt="80", pb="80")

    def stat_cell(num, label, border=True):
        border_css = "border-right:1px solid rgba(255,255,255,0.05);" if border else ""
        return html_w(f'<div style="text-align:center;padding:40px;{border_css}"><p style="color:#FACC15;font-family:Montserrat,sans-serif;font-weight:900;font-size:48px;margin:0 0 8px;line-height:1;">{num}</p><p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:1px;margin:0;">{label}</p></div>')
    stats_sec = sec([
        col([stat_cell("2026", "Year of Launch")], 25),
        col([stat_cell("AC", "Atlantic City Based")], 25),
        col([stat_cell("12+", "Events Planned 2026")], 25),
        col([stat_cell("100%", "Jersey Shore Energy", False)], 25),
    ], bg="#121826", pt="0", pb="0")

    founder_html = """<div style="background:#1A2233;border:1px solid rgba(255,255,255,0.07);border-radius:16px;padding:40px;max-width:900px;margin:0 auto;">
  <div style="display:flex;flex-wrap:wrap;gap:32px;align-items:flex-start;">
    <div style="flex:0 0 120px;text-align:center;">
      <div style="width:120px;height:120px;border-radius:50%;background:#0B0F14;border:3px solid #FACC15;display:flex;align-items:center;justify-content:center;font-size:52px;margin:0 auto 12px;">🤵</div>
    </div>
    <div style="flex:1;min-width:240px;">
      <h3 style="color:#fff;font-family:Montserrat,sans-serif;font-weight:900;font-size:28px;text-transform:uppercase;margin:0 0 4px;">Rico</h3>
      <p style="color:#FACC15;font-family:Inter,sans-serif;font-size:12px;font-weight:700;text-transform:uppercase;letter-spacing:2px;margin:0 0 16px;">Founder &amp; Event Director</p>
      <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:14px;line-height:1.8;margin:0 0 12px;">Born and raised with deep roots in the Jersey Shore, Rico built Party Like Rico Promotions from a simple belief: Atlantic City deserves world-class events and experiences that bring people together.</p>
      <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:14px;line-height:1.8;margin:0 0 20px;">With a passion for nightlife, community, and culture — Rico brings the vision, the hustle, and the network to every single event.</p>
      <div style="display:flex;gap:8px;flex-wrap:wrap;">
        <a href="#ig" style="background:transparent;border:1px solid rgba(255,255,255,0.2);color:#9CA3AF;text-decoration:none;padding:8px 16px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;">Instagram</a>
        <a href="#fb" style="background:transparent;border:1px solid rgba(255,255,255,0.2);color:#9CA3AF;text-decoration:none;padding:8px 16px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;">Facebook</a>
        <a href="mailto:PartyLikeRico@gmail.com" style="background:transparent;border:1px solid rgba(255,255,255,0.2);color:#9CA3AF;text-decoration:none;padding:8px 16px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;">Email Rico</a>
      </div>
    </div>
  </div>
</div>"""
    founder_sec = sec([col([
        label_pill("THE TEAM", "#FACC15"), spacer(8),
        heading('THE PEOPLE BEHIND THE <span style="color:#FACC15;">BRAND</span>', "h2", "center", "#FFFFFF", 48),
        spacer(32), html_w(founder_html),
    ])], bg="#060a06", pt="80", pb="80")

    rico_html = """<div style="max-width:1000px;margin:0 auto;">
  <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:rgba(250,204,21,0.15);border:1px solid rgba(250,204,21,0.2);border-radius:16px;overflow:hidden;margin-bottom:32px;">
    <div style="background:#0B1A0B;padding:40px;text-align:center;"><p style="color:#FACC15;font-family:Montserrat,sans-serif;font-weight:900;font-size:96px;margin:0 0 8px;line-height:1;">R</p><p style="color:#FACC15;font-family:Montserrat,sans-serif;font-weight:700;font-size:18px;margin:0 0 6px;text-transform:uppercase;">Realize</p><p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:2px;margin:0;">The Vision</p></div>
    <div style="background:#0B1A0B;padding:40px;text-align:center;border-left:1px solid rgba(250,204,21,0.15);"><p style="color:#FACC15;font-family:Montserrat,sans-serif;font-weight:900;font-size:96px;margin:0 0 8px;line-height:1;">I</p><p style="color:#FACC15;font-family:Montserrat,sans-serif;font-weight:700;font-size:18px;margin:0 0 6px;text-transform:uppercase;">Individuals</p><p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:2px;margin:0;">The People</p></div>
    <div style="background:#0B1A0B;padding:40px;text-align:center;border-left:1px solid rgba(250,204,21,0.15);"><p style="color:#FACC15;font-family:Montserrat,sans-serif;font-weight:900;font-size:96px;margin:0 0 8px;line-height:1;">C</p><p style="color:#FACC15;font-family:Montserrat,sans-serif;font-weight:700;font-size:18px;margin:0 0 6px;text-transform:uppercase;">Celebrate</p><p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:2px;margin:0;">The Moments</p></div>
    <div style="background:#0B1A0B;padding:40px;text-align:center;border-left:1px solid rgba(250,204,21,0.15);"><p style="color:#FACC15;font-family:Montserrat,sans-serif;font-weight:900;font-size:96px;margin:0 0 8px;line-height:1;">O</p><p style="color:#FACC15;font-family:Montserrat,sans-serif;font-weight:700;font-size:18px;margin:0 0 6px;text-transform:uppercase;">Occasions</p><p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:2px;margin:0;">The Events</p></div>
  </div>
  <p style="text-align:center;color:#9CA3AF;font-family:Inter,sans-serif;font-size:15px;line-height:1.8;max-width:600px;margin:0 auto;">Every letter carries meaning. Every event carries purpose. When you party with Rico, you're part of something bigger than a night out.</p>
</div>"""
    acronym_sec = sec([col([
        label_pill("THE NAME", "#FACC15"), spacer(8),
        heading('BEHIND THE NAME <span style="color:#FACC15;">RICO</span>', "h2", "center", "#FFFFFF", 48),
        spacer(32), html_w(rico_html),
    ])], bg="#0a1a0a", pt="80", pb="80")

    def val_card(icon, title, body):
        return html_w(f"""<div style="background:#1A2233;border:1px solid rgba(255,255,255,0.07);border-radius:14px;padding:28px;height:100%;transition:all 0.3s ease;" onmouseover="this.style.transform='translateY(-4px)';this.style.borderColor='rgba(250,204,21,0.2)';" onmouseout="this.style.transform='translateY(0)';this.style.borderColor='rgba(255,255,255,0.07)';">
  <div style="font-size:36px;margin-bottom:16px;">{icon}</div>
  <h4 style="color:#fff;font-family:Montserrat,sans-serif;font-weight:700;font-size:16px;text-transform:uppercase;margin:0 0 10px;">{title}</h4>
  <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:13px;line-height:1.7;margin:0;">{body}</p>
</div>""")

    val_header = sec([col([
        label_pill("WHAT DRIVES US", "#F97316"), spacer(8),
        heading('OUR BRAND <span style="color:#FACC15;">VALUES</span>', "h2", "center", "#FFFFFF", 48),
        spacer(32),
    ])], bg="#0B0F14", pt="80", pb="0")
    val_r1 = sec([
        col([val_card("🔥", "Energy &amp; Excitement", "We bring high-energy, unforgettable atmospheres to every event we touch.")], 33),
        col([val_card("🤝", "Community First", "Everything we do is rooted in lifting up and celebrating the Atlantic City community.")], 33),
        col([val_card("⭐", "Premium Experiences", "We don't do average. Every detail is crafted for maximum impact and memory.")], 33),
    ], bg="#0B0F14", pt="0", pb="20")
    val_r2 = sec([
        col([val_card("🌊", "Shore Town Roots", "We're proudly rooted in the Jersey Shore — and that energy lives in everything we create.")], 33),
        col([val_card("🎯", "Results-Driven", "Packed events, brand growth, and satisfied partners — results speak louder than promises.")], 33),
        col([val_card("📣", "Bold Promotion", "We promote loud, proud, and with purpose. Your event deserves to be heard.")], 33),
    ], bg="#0B0F14", pt="20", pb="80")

    cta_sec = sec([col([
        label_pill("JOIN US", "#F97316"), spacer(8),
        heading('READY TO PARTY LIKE <span style="color:#FACC15;">RICO</span>?', "h2", "center", "#FFFFFF", 48),
        spacer(16),
        text_editor("Join us at our next event, become a vendor partner, or reach out. Atlantic City is waiting.", "#9CA3AF", 16, "center"),
        spacer(24),
        btn_row(link_btn("🎟 Buy Tickets", PAYPAL),
                link_btn("Become a Partner", "/vendor", outline=True)),
    ])], bg="#060a06", pt="80", pb="80")

    return page_struct("About | Party Like Rico",
                       [hero, intro_sec, stats_sec, founder_sec, acronym_sec,
                        val_header, val_r1, val_r2, cta_sec])


# ============================================================
# PAGE 6: BLOG PAGE
# ============================================================

def build_blog():
    reset_ids()

    hero = hero_section("NEWS · UPDATES · GUIDES", "#FACC15", "BLOG &amp; NEWS",
        "Your insider guide to Atlantic City events, local highlights, upcoming experiences, "
        "and everything Party Like Rico.")

    feat_html = f"""<div style="background:#1A2233;border:1px solid rgba(255,255,255,0.07);border-radius:16px;overflow:hidden;display:flex;flex-wrap:wrap;max-width:1100px;margin:0 auto;">
  <div style="flex:0 0 40%;min-width:280px;background:#111;display:flex;align-items:center;justify-content:center;min-height:300px;">
    <span style="font-size:80px;">📰</span>
  </div>
  <div style="flex:1;padding:40px;min-width:280px;">
    <span style="display:inline-block;background:#FACC1522;color:#FACC15;border:1px solid #FACC1555;padding:5px 16px;border-radius:50px;font-family:Inter,sans-serif;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:16px;">⭐ Featured Article</span>
    <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:13px;margin:0 0 12px;">📅 March 2026 &nbsp;·&nbsp; ✍️ Party Like Rico Team &nbsp;·&nbsp; ⏱️ 5 min read</p>
    <h2 style="font-family:Montserrat,sans-serif;font-weight:900;text-transform:uppercase;color:#fff;font-size:28px;line-height:1.2;margin:0 0 16px;">Welcome to Party Like Rico Promotions — Atlantic City's New Event Experience</h2>
    <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:14px;line-height:1.7;margin:0 0 24px;">Get the inside story on who we are, what we do, and why Atlantic City needed a promotion company like Party Like Rico. From bud crawls to nightlife — we're just getting started.</p>
    <a href="/blog/welcome" style="display:inline-block;background:#F97316;color:#fff;text-decoration:none;padding:14px 28px;border-radius:50px;font-family:Inter,sans-serif;font-size:13px;font-weight:700;text-transform:uppercase;">Read Full Article →</a>
  </div>
</div>"""
    feat_sec = sec([col([html_w(feat_html)])], bg="#0B0F14", pt="80", pb="80")

    def blog_card(tag, tc, meta, title, excerpt):
        return (f'<div style="background:#0e1218;border:1px solid rgba(255,255,255,0.06);border-radius:14px;'
                f'overflow:hidden;margin-bottom:24px;transition:all 0.3s ease;" '
                f'onmouseover="this.style.transform=\'translateY(-4px)\';this.style.boxShadow=\'0 16px 40px rgba(0,0,0,0.4)\';" '
                f'onmouseout="this.style.transform=\'translateY(0)\';this.style.boxShadow=\'none\';">'
                f'<div style="aspect-ratio:16/10;background:#111;display:flex;align-items:center;justify-content:center;">'
                f'<span style="font-size:40px;">📝</span></div>'
                f'<div style="padding:20px;">'
                f'<span style="display:inline-block;background:{tc}22;color:{tc};border:1px solid {tc}55;'
                f'padding:3px 10px;border-radius:50px;font-family:Inter,sans-serif;font-size:11px;'
                f'font-weight:700;text-transform:uppercase;margin-bottom:10px;">{tag}</span>'
                f'<h4 style="color:#fff;font-family:Montserrat,sans-serif;font-weight:700;font-size:15px;'
                f'text-transform:uppercase;margin:0 0 8px;line-height:1.3;">{title}</h4>'
                f'<p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:13px;line-height:1.6;margin:0 0 16px;">{excerpt}</p>'
                f'<div style="display:flex;align-items:center;justify-content:space-between;padding-top:12px;border-top:1px solid rgba(255,255,255,0.06);">'
                f'<span style="color:#9CA3AF;font-size:12px;font-family:Inter,sans-serif;">{meta}</span>'
                f'<a href="#" style="color:#FACC15;font-family:Inter,sans-serif;font-size:12px;font-weight:700;text-decoration:none;">Read →</a>'
                f'</div></div></div>')

    cards_html = (
        blog_card("Event Updates", "#22C55E", "March 2026 · 4 min",
                  "Everything You Need to Know About the 420 Weekend AC Bud Crawl",
                  "Date, time, tickets, locations — your complete guide to the biggest 420 event in Atlantic City.") +
        blog_card("AC News", "#3B82F6", "February 2026 · 6 min",
                  "The Best Things to Do in Atlantic City in 2026 — Beyond the Casino",
                  "AC has way more to offer than the casino floor. Here's your guide to the best experiences.") +
        blog_card("Partner Spotlights", "#A855F7", "January 2026 · 5 min",
                  "Why Local Businesses Should Partner with Party Like Rico",
                  "Reach Atlantic City's most engaged audience and grow your brand through strategic event partnerships.") +
        blog_card("Upcoming Experiences", "#FACC15", "Coming Soon · 3 min",
                  "Summer 2026 Events Preview — What's Coming to Atlantic City",
                  "Get an early look at the summer lineup — new events, new venues, new vibes coming to AC.") +
        blog_card("Local Highlights", "#06B6D4", "Coming Soon · 4 min",
                  "Planning a Birthday, Bachelorette, or Private Celebration in AC?",
                  "Atlantic City is the perfect backdrop for a private event. Here's how Party Like Rico can help.") +
        blog_card("AC News", "#3B82F6", "Coming Soon · 7 min",
                  "The Ultimate Atlantic City Weekend Itinerary — RICO Edition",
                  "From Friday night to Sunday morning — the definitive Party Like Rico guide to a weekend in AC.")
    )

    sidebar_html = f"""<div style="display:flex;flex-direction:column;gap:20px;">
  <div style="background:#1A2233;border:1px solid rgba(255,255,255,0.07);border-radius:12px;padding:20px;">
    <input type="text" placeholder="Search articles..." style="width:100%;background:#0B0F14;border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:12px 16px;color:#fff;font-family:Inter,sans-serif;font-size:14px;outline:none;box-sizing:border-box;" />
  </div>
  <div style="background:#1A2233;border:1px solid rgba(255,255,255,0.07);border-radius:12px;padding:20px;">
    <p style="color:#fff;font-family:Montserrat,sans-serif;font-weight:700;font-size:14px;text-transform:uppercase;margin:0 0 14px;">Categories</p>
    <div style="display:flex;flex-wrap:wrap;gap:8px;">
      <span style="background:#22C55E22;color:#22C55E;border:1px solid #22C55E44;padding:4px 12px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;cursor:pointer;">Event Updates</span>
      <span style="background:#3B82F622;color:#3B82F6;border:1px solid #3B82F644;padding:4px 12px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;cursor:pointer;">AC News</span>
      <span style="background:#FACC1522;color:#FACC15;border:1px solid #FACC1544;padding:4px 12px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;cursor:pointer;">Guides</span>
      <span style="background:#A855F722;color:#A855F7;border:1px solid #A855F744;padding:4px 12px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;cursor:pointer;">Nightlife</span>
      <span style="background:#F9731622;color:#F97316;border:1px solid #F9731644;padding:4px 12px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;cursor:pointer;">Partner Spotlights</span>
    </div>
  </div>
  <div style="background:#1A2233;border:2px solid #22C55E;border-radius:12px;padding:20px;">
    <span style="display:inline-block;background:#22C55E22;color:#22C55E;border:1px solid #22C55E55;padding:3px 10px;border-radius:50px;font-family:Inter,sans-serif;font-size:11px;font-weight:700;text-transform:uppercase;margin-bottom:10px;">🌿 Featured Event</span>
    <h4 style="color:#fff;font-family:Montserrat,sans-serif;font-weight:700;font-size:14px;text-transform:uppercase;margin:0 0 6px;">420 Weekend AC Bud Crawl</h4>
    <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:12px;margin:0 0 4px;">📅 April 18, 2026</p>
    <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:12px;margin:0 0 14px;">💵 $25 · 21+ Only</p>
    <a href="{PAYPAL}" style="display:inline-block;background:#F97316;color:#fff;text-decoration:none;padding:10px 20px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;text-transform:uppercase;">🎟 Buy Tickets</a>
  </div>
  <div style="background:#1A2233;border:2px solid #FACC15;border-radius:12px;padding:20px;">
    <p style="color:#FACC15;font-family:Montserrat,sans-serif;font-weight:700;font-size:14px;text-transform:uppercase;margin:0 0 6px;">Newsletter</p>
    <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:13px;margin:0 0 14px;">Get event updates, exclusive offers, and more delivered to your inbox.</p>
    <div style="border:2px dashed rgba(250,204,21,0.3);border-radius:8px;padding:16px;text-align:center;">
      <code style="color:#FACC15;font-family:monospace;font-size:12px;">[wpforms id="newsletter-form-id"]</code>
    </div>
  </div>
</div>"""

    blog_layout = sec([col([html_w(cards_html)], 67), col([html_w(sidebar_html)], 33)],
                      bg="#0B0F14", pt="80", pb="80")

    cta_sec = sec([col([
        label_pill("GET FEATURED", "#F97316"), spacer(8),
        heading('HAVE A STORY TO <span style="color:#FACC15;">SHARE</span>?', "h2", "center", "#FFFFFF", 48),
        spacer(16),
        text_editor("Have an event, a brand, or a story that deserves to be heard in Atlantic City? Reach out — we'd love to feature you.", "#9CA3AF", 16, "center"),
        spacer(24),
        btn_row(link_btn("Get Featured", "/contact"),
                link_btn("View Events", "/events", outline=True)),
    ])], bg="#121826", pt="80", pb="80")

    return page_struct("Blog & News | Party Like Rico", [hero, feat_sec, blog_layout, cta_sec])


# ============================================================
# PAGE 7: SHOP PAGE
# ============================================================

def build_shop():
    reset_ids()

    # Countdown hero — no f-string so JS curly braces are safe
    countdown_html = """<div style="max-width:700px;margin:0 auto;padding:80px 20px;text-align:center;">
  <style>@keyframes plrpulse{0%,100%{box-shadow:0 0 0 0 rgba(250,204,21,0.4);}50%{box-shadow:0 0 0 14px rgba(250,204,21,0);}}</style>
  <span style="display:inline-block;background:rgba(250,204,21,0.1);color:#FACC15;border:1px solid rgba(250,204,21,0.3);padding:8px 24px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:28px;animation:plrpulse 2s infinite;">🛍️ SHOP — COMING SOON</span>
  <h1 style="font-family:Montserrat,sans-serif;font-weight:900;text-transform:uppercase;color:#fff;font-size:64px;line-height:1.1;margin:0 0 20px;">OFFICIAL PARTY LIKE RICO <span style="color:#FACC15;">MERCH</span></h1>
  <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:17px;line-height:1.7;margin:0 0 32px;">Represent Atlantic City's most exciting event brand. Limited edition drops, exclusive event gear, and branded apparel are on the way.</p>
  <div style="background:#1A2233;border:2px dashed rgba(250,204,21,0.3);border-radius:12px;padding:24px;margin-bottom:36px;">
    <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:13px;margin:0 0 8px;">Get notified when we launch — be first to shop:</p>
    <code style="color:#FACC15;font-family:monospace;font-size:14px;">[wpforms id="shop-notify-form-id"]</code>
  </div>
  <div style="display:flex;justify-content:center;gap:16px;flex-wrap:wrap;margin-bottom:24px;">
    <div style="background:#1A2233;border:1px solid rgba(255,255,255,0.07);border-radius:12px;padding:20px 28px;min-width:90px;text-align:center;">
      <p id="plr-days" style="color:#FACC15;font-family:Montserrat,sans-serif;font-weight:900;font-size:48px;margin:0;line-height:1;">00</p>
      <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:2px;margin:6px 0 0;">Days</p>
    </div>
    <div style="background:#1A2233;border:1px solid rgba(255,255,255,0.07);border-radius:12px;padding:20px 28px;min-width:90px;text-align:center;">
      <p id="plr-hours" style="color:#FACC15;font-family:Montserrat,sans-serif;font-weight:900;font-size:48px;margin:0;line-height:1;">00</p>
      <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:2px;margin:6px 0 0;">Hours</p>
    </div>
    <div style="background:#1A2233;border:1px solid rgba(255,255,255,0.07);border-radius:12px;padding:20px 28px;min-width:90px;text-align:center;">
      <p id="plr-mins" style="color:#FACC15;font-family:Montserrat,sans-serif;font-weight:900;font-size:48px;margin:0;line-height:1;">00</p>
      <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:2px;margin:6px 0 0;">Mins</p>
    </div>
    <div style="background:#1A2233;border:1px solid rgba(255,255,255,0.07);border-radius:12px;padding:20px 28px;min-width:90px;text-align:center;">
      <p id="plr-secs" style="color:#FACC15;font-family:Montserrat,sans-serif;font-weight:900;font-size:48px;margin:0;line-height:1;">00</p>
      <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:2px;margin:6px 0 0;">Secs</p>
    </div>
  </div>
  <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:13px;margin:0;">Targeting a <strong style="color:#FACC15;">Summer 2026</strong> launch</p>
</div>
<script>
(function(){
  var target=new Date("June 1, 2026 00:00:00").getTime();
  function pad(n){return String(n).padStart(2,"0");}
  function tick(){
    var diff=target-Date.now();
    if(diff<0){diff=0;}
    var d=Math.floor(diff/86400000);
    var h=Math.floor((diff%86400000)/3600000);
    var m=Math.floor((diff%3600000)/60000);
    var s=Math.floor((diff%60000)/1000);
    var el=document.getElementById("plr-days");
    if(el){el.textContent=pad(d);}
    el=document.getElementById("plr-hours");
    if(el){el.textContent=pad(h);}
    el=document.getElementById("plr-mins");
    if(el){el.textContent=pad(m);}
    el=document.getElementById("plr-secs");
    if(el){el.textContent=pad(s);}
  }
  tick();setInterval(tick,1000);
})();
</script>"""
    hero_sec = sec([col([html_w(countdown_html)])], bg="#030b03", pt="0", pb="0")

    def cat_card(icon, title, body):
        return html_w(f"""<div style="background:#1A2233;border:1px solid rgba(255,255,255,0.07);border-radius:14px;padding:28px;text-align:center;height:100%;transition:all 0.3s ease;" onmouseover="this.style.transform='translateY(-4px)';this.style.borderColor='rgba(250,204,21,0.3)';" onmouseout="this.style.transform='translateY(0)';this.style.borderColor='rgba(255,255,255,0.07)';">
  <div style="font-size:40px;margin-bottom:14px;">{icon}</div>
  <h4 style="color:#fff;font-family:Montserrat,sans-serif;font-weight:700;font-size:15px;text-transform:uppercase;margin:0 0 8px;">{title}</h4>
  <p style="color:#9CA3AF;font-family:Inter,sans-serif;font-size:13px;line-height:1.6;margin:0;">{body}</p>
</div>""")

    cat_header = sec([col([
        label_pill("WHAT'S COMING", "#FACC15"), spacer(8),
        heading('MERCH <span style="color:#FACC15;">CATEGORIES</span>', "h2", "center", "#FFFFFF", 48),
        spacer(32),
    ])], bg="#121826", pt="80", pb="0")
    cat_grid = sec([
        col([cat_card("👕", "Apparel", "Tees, hoodies, and event-specific drops")], 25),
        col([cat_card("🧢", "Headwear", "Fitted caps, snapbacks, and branded hats")], 25),
        col([cat_card("🎟", "Event Gear", "Limited edition event merch and collectibles")], 25),
        col([cat_card("🛍", "Accessories", "Bags, lanyards, stickers, and branded items")], 25),
    ], bg="#121826", pt="0", pb="80")

    def product_card(icon, name, price, badge, bc):
        return html_w(f"""<div style="background:#1A2233;border:1px solid rgba(255,255,255,0.07);border-radius:14px;overflow:hidden;transition:all 0.3s ease;" onmouseover="this.style.transform='translateY(-4px)';this.style.boxShadow='0 16px 40px rgba(0,0,0,0.4)';" onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='none';">
  <div style="position:relative;aspect-ratio:1;background:#111;display:flex;align-items:center;justify-content:center;">
    <span style="font-size:60px;opacity:0.5;">{icon}</span>
    <div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;"><span style="font-size:36px;background:rgba(0,0,0,0.5);border-radius:50%;width:70px;height:70px;display:flex;align-items:center;justify-content:center;">🔒</span></div>
    <span style="position:absolute;top:10px;right:10px;background:{bc}22;color:{bc};border:1px solid {bc}55;padding:3px 10px;border-radius:50px;font-family:Inter,sans-serif;font-size:10px;font-weight:700;text-transform:uppercase;">{badge}</span>
  </div>
  <div style="padding:16px;text-align:center;">
    <h4 style="color:#fff;font-family:Montserrat,sans-serif;font-weight:700;font-size:14px;text-transform:uppercase;margin:0 0 4px;">{name}</h4>
    <p style="color:#FACC15;font-family:Inter,sans-serif;font-size:15px;font-weight:700;margin:0 0 12px;">Starting at {price}</p>
    <button disabled style="width:100%;background:transparent;color:#9CA3AF;border:2px dashed rgba(255,255,255,0.15);padding:10px;border-radius:50px;font-family:Inter,sans-serif;font-size:12px;font-weight:700;text-transform:uppercase;cursor:not-allowed;">🔒 Available at Launch</button>
  </div>
</div>""")

    locked_header = sec([col([
        label_pill("SNEAK PEEK", "#FACC15"), spacer(8),
        heading('COMING TO THE <span style="color:#FACC15;">SHOP</span>', "h2", "center", "#FFFFFF", 48),
        spacer(8),
        text_editor("These items are locked until launch — sign up above to be notified first.", "#9CA3AF", 15, "center"),
        spacer(32),
    ])], bg="#0B0F14", pt="80", pb="0")
    locked_r1 = sec([
        col([product_card("👕", "PLR Classic Tee", "$29.99", "Coming Soon", "#FACC15")], 33),
        col([product_card("🧥", "PLR Hoodie", "$54.99", "Limited", "#FACC15")], 33),
        col([product_card("🧢", "PLR Snapback Cap", "$24.99", "Fan Fav", "#FACC15")], 33),
    ], bg="#0B0F14", pt="0", pb="20")
    locked_r2 = sec([
        col([product_card("🌿", "420 Bud Crawl Event Tee", "$32.99", "Event Drop", "#22C55E")], 33),
        col([product_card("🎒", "PLR Tote Bag", "$19.99", "New", "#FACC15")], 33),
        col([product_card("🎁", "PLR Starter Bundle", "$69.99", "Bundle", "#FACC15")], 33),
    ], bg="#0B0F14", pt="20", pb="80")

    final_sec = sec([col([
        label_pill("CAN'T WAIT?", "#F97316"), spacer(8),
        heading('BUY TICKETS <span style="color:#FACC15;">NOW</span>', "h2", "center", "#FFFFFF", 48),
        spacer(16),
        text_editor("The shop is coming — but our next event is April 18, 2026. Secure your spot today.", "#9CA3AF", 16, "center"),
        spacer(24),
        btn_row(link_btn("🎟 Buy Tickets — $25", PAYPAL),
                link_btn("View All Events", "/events", outline=True)),
    ])], bg="#121826", pt="80", pb="80")

    return page_struct("Merch Shop | Party Like Rico",
                       [hero_sec, cat_header, cat_grid, locked_header, locked_r1, locked_r2, final_sec])


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    OUT = "plr-elementor-pages"
    os.makedirs(OUT, exist_ok=True)

    pages = [
        ("events-page.json",  build_events,  "Events"),
        ("media-page.json",   build_media,   "Media & Gallery"),
        ("promote-page.json", build_promote, "Promote With Rico"),
        ("contact-page.json", build_contact, "Contact Us"),
        ("about-page.json",   build_about,   "About Party Like Rico"),
        ("blog-page.json",    build_blog,    "Blog & News"),
        ("shop-page.json",    build_shop,    "Merch Shop"),
    ]

    summary = []
    for fname, builder, label in pages:
        data = builder()
        raw = json.dumps(data, indent=2, ensure_ascii=False)
        json.loads(raw)   # validate
        path = os.path.join(OUT, fname)
        with open(path, "w", encoding="utf-8") as f:
            f.write(raw)
        nsec = len(data["content"])
        kb   = round(len(raw.encode("utf-8")) / 1024, 1)
        summary.append((fname, kb, nsec, label))
        print(f"  OK  {fname}  ({kb}KB, {nsec} sections)")

    zip_path = "plr-elementor-pages.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for fname, *_ in summary:
            zf.write(os.path.join(OUT, fname), fname)
    zip_kb = round(os.path.getsize(zip_path) / 1024, 1)

    print()
    print("=" * 65)
    print("  PARTY LIKE RICO — ELEMENTOR TEMPLATES COMPLETE")
    print("=" * 65)
    print(f"  {'File':<30} {'Size':>7}  {'Sections':>9}  Page")
    print("  " + "-" * 62)
    for fname, kb, nsec, label in summary:
        print(f"  {fname:<30} {kb:>5.1f}KB  {nsec:>8}  {label}")
    print("  " + "-" * 62)
    print(f"  ZIP: {zip_path}  ({zip_kb}KB)")
    print()
    print("  Import: WordPress > Elementor > Templates > Import Template")
    print("=" * 65)
