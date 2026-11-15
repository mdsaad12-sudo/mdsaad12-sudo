"""Render animated SVG cards for the GitHub profile README.
Run: python scripts/render_cards.py   (writes ./cards/*.svg)
SVGs are self-contained: CSS keyframes only, system fonts, no scripts.
"""
import os, html
OUT = os.path.join(os.path.dirname(__file__), "..", "cards")
os.makedirs(OUT, exist_ok=True)

BG, PANEL, LINE = "#0b1220", "#111a2e", "#1f2d4a"
CY, GR, PU, TX, MUT = "#22d3ee", "#34d399", "#a78bfa", "#e6edf7", "#7d8cab"
MONO = "ui-monospace,SFMono-Regular,Consolas,'Courier New',monospace"
SANS = "'Segoe UI',system-ui,-apple-system,Helvetica,Arial,sans-serif"
e = html.escape

def wrap(w, h, body, css=""):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">
<style>
text{{font-family:{SANS}}} .m{{font-family:{MONO}}}
@keyframes rise{{from{{opacity:0;transform:translateY(14px)}}to{{opacity:1;transform:none}}}}
@keyframes blink{{50%{{opacity:0}}}}
@keyframes pulse{{0%{{r:5;opacity:.9}}100%{{r:22;opacity:0}}}}
@keyframes sweep{{from{{transform:translateX(-120%)}}to{{transform:translateX(320%)}}}}
@keyframes grow{{from{{transform:scaleX(0)}}to{{transform:scaleX(1)}}}}
@keyframes type{{from{{clip-path:inset(0 100% 0 0)}}to{{clip-path:inset(0 0 0 0)}}}}
@keyframes drift{{from{{transform:translateY(0)}}to{{transform:translateY(8px)}}}}
@keyframes pop{{0%{{transform:scale(.7);opacity:0}}70%{{transform:scale(1.06);opacity:1}}100%{{transform:scale(1)}}}}
.r{{opacity:0;animation:rise .7s cubic-bezier(.2,.8,.2,1) forwards}}
.bl{{animation:blink 1s steps(1) infinite}}
.ty{{animation:type 1.4s steps(34) forwards;clip-path:inset(0 100% 0 0)}}
.gr{{transform-box:fill-box;transform-origin:left;animation:grow 1.2s cubic-bezier(.2,.8,.2,1) forwards;transform:scaleX(0)}}
.sw{{animation:sweep 4s ease-in-out infinite}}
.pp{{transform-box:fill-box;transform-origin:center;animation:pop .6s ease-out forwards;opacity:0}}
{css}
@media (prefers-reduced-motion:reduce){{.r,.pp,.gr,.sc,.bl,[style*=animation]{{animation:none!important;opacity:1!important;transform:none!important}}.gr{{transform:scaleX(1)!important}}.sw{{display:none}}[style*=pulse]{{display:none}}}}
</style>
<defs>
<linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="{CY}"/><stop offset="1" stop-color="{GR}"/></linearGradient>
<linearGradient id="sh" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".12"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<clipPath id="c"><rect width="{w}" height="{h}" rx="16"/></clipPath>
</defs>
<rect width="{w}" height="{h}" rx="16" fill="{BG}"/>
<rect x=".5" y=".5" width="{w-1}" height="{h-1}" rx="16" fill="none" stroke="{LINE}"/>
{body}
</svg>'''

def save(name, svg):
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(svg)

# ---------- HERO ----------
def hero():
    w, h = 900, 320
    b = ""
    for x in range(30, w, 40):
        for y in range(70, h, 40):
            b += f'<circle cx="{x}" cy="{y}" r="1" fill="{LINE}"/>'
    for i, c in enumerate(("#ff5f56", "#ffbd2e", "#27c93f")):
        b += f'<circle cx="{30+i*20}" cy="28" r="6" fill="{c}"/>'
    b += f'<text x="{w-30}" y="32" text-anchor="end" class="m" font-size="12" fill="{MUT}">~/mdsaad12-sudo</text>'
    b += f'<line x1="0" x2="{w}" y1="50" y2="50" stroke="{LINE}"/>'
    b += f'<g class="r" style="animation-delay:.1s"><text x="40" y="112" font-size="48" font-weight="800" fill="url(#g)">MOHAMMED SAAD R</text></g>'
    b += f'<g class="r" style="animation-delay:.4s"><text x="42" y="144" font-size="17" fill="{MUT}">Cybersecurity student · ethical hacking · defensive tooling</text></g>'
    rows = [
        ("whoami", "mohammed-saad-r", 1.0),
        ("cat focus.txt", "cybersecurity · networking labs · AI security", 1.9),
        ("ls projects/", "core0  pay-guard  desktop-buddy  malware-lifecycle-lab", 2.8),
    ]
    y = 192
    for cmd, out, d in rows:
        b += f'<g class="r" style="animation-delay:{d}s"><text class="m" x="42" y="{y}" font-size="14"><tspan fill="{GR}">$ </tspan><tspan fill="{TX}">{e(cmd)}</tspan></text></g>'
        b += f'<g class="r" style="animation-delay:{d+.4}s"><text class="m" x="240" y="{y}" font-size="14" fill="{CY}">{e(out)}</text></g>'
        y += 30
    b += f'<g class="r" style="animation-delay:3.6s"><text class="m" x="42" y="{y}" font-size="14" fill="{GR}">$ <tspan class="bl" fill="{CY}">█</tspan></text></g>'
    # shine bar under name
    b += f'<g clip-path="url(#c)"><rect y="50" width="120" height="2" fill="url(#g)" class="sw"/></g>'
    # shield glyph right
    b += f'''<g transform="translate(740 120)"><g style="animation:drift 3s ease-in-out infinite alternate">
<path d="M60 0 L120 20 V70 C120 110 90 135 60 150 C30 135 0 110 0 70 V20 Z" fill="{PANEL}" stroke="url(#g)" stroke-width="2.5"/>
<path d="M38 74 L55 92 L86 56" fill="none" stroke="{GR}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="60" cy="75" r="5" fill="none" stroke="{CY}" style="animation:pulse 2.4s ease-out infinite"/></g></g>'''
    return wrap(w, h, b)

# ---------- TILES ----------
def tile(name, icon_label, title, items, color, delay):
    w, h = 290, 190
    b = f'<g clip-path="url(#c)"><rect y="0" width="70" height="{h}" fill="url(#sh)" class="sw" style="animation-delay:{delay}s"/></g>'
    b += f'<g class="pp" style="animation-delay:{delay}s"><rect x="24" y="24" width="44" height="44" rx="12" fill="{PANEL}" stroke="{color}"/>'
    b += f'<text x="46" y="53" text-anchor="middle" font-size="20" font-weight="700" fill="{color}">{icon_label}</text></g>'
    b += f'<circle cx="46" cy="46" r="5" fill="none" stroke="{color}" style="animation:pulse 2.8s ease-out infinite;animation-delay:{delay}s"/>'
    b += f'<g class="r" style="animation-delay:{delay+.2}s"><text x="82" y="42" font-size="11" letter-spacing="3" fill="{color}" font-weight="700">{e(name)}</text>'
    b += f'<text x="82" y="62" font-size="17" font-weight="700" fill="{TX}">{e(title)}</text></g>'
    y = 98
    for i, (label, pct) in enumerate(items):
        d = delay + .4 + i * .2
        b += f'<g class="r" style="animation-delay:{d}s"><text x="24" y="{y}" font-size="12" fill="{MUT}">{e(label)}</text></g>'
        b += f'<rect x="24" y="{y+7}" width="242" height="5" rx="2.5" fill="{PANEL}"/>'
        b += f'<rect x="24" y="{y+7}" width="{242*pct/100:.0f}" height="5" rx="2.5" fill="{color}" class="gr" style="animation-delay:{d}s"/>'
        y += 28
    return wrap(w, h, b)

# ---------- REPO CARDS ----------
def repo(name, desc, lang, color, delay, tag):
    w, h = 440, 150
    words, lines, cur = desc.split(), [], ""
    for wd in words:
        if len(cur) + len(wd) > 58:
            lines.append(cur); cur = wd
        else:
            cur = (cur + " " + wd).strip()
    lines.append(cur)
    lines = lines[:3]
    b = f'<rect x="0" y="0" width="5" height="{h}" fill="{color}" clip-path="url(#c)"/>'
    b += f'<g clip-path="url(#c)"><rect y="0" width="90" height="{h}" fill="url(#sh)" class="sw" style="animation-delay:{delay}s"/></g>'
    b += f'<g class="r" style="animation-delay:{delay}s"><text class="m" x="28" y="38" font-size="17" font-weight="700" fill="{TX}">{e(name)}</text>'
    b += f'<text x="{w-24}" y="36" text-anchor="end" font-size="10" letter-spacing="2" fill="{color}" font-weight="700">{e(tag)}</text></g>'
    for i, ln in enumerate(lines):
        b += f'<g class="r" style="animation-delay:{delay+.2+i*.1}s"><text x="28" y="{66+i*20}" font-size="13" fill="{MUT}">{e(ln)}</text></g>'
    b += f'<g class="r" style="animation-delay:{delay+.6}s"><circle cx="32" cy="{h-24}" r="5" fill="{color}"/><text x="46" y="{h-20}" font-size="12" fill="{TX}">{e(lang)}</text></g>'
    return wrap(w, h, b)

# ---------- STACK STRIP ----------
def stack():
    w, h = 900, 110
    tags = ["C", "Python", "Linux", "Networking", "Splunk", "Ethical Hacking", "Flask", "JavaScript", "AWS", "Cloudflare", "Wireshark", "Cisco PT"]
    row = ""
    x = 0
    for t in tags:
        tw = 24 + len(t) * 8
        row += f'<rect x="{x}" y="0" width="{tw}" height="34" rx="17" fill="{PANEL}" stroke="{LINE}"/><text x="{x+tw/2}" y="22" text-anchor="middle" font-size="13" fill="{TX}">{e(t)}</text>'
        x += tw + 12
    total = x
    css = f"@keyframes scroll{{from{{transform:translateX(0)}}to{{transform:translateX(-{total}px)}}}} .sc{{animation:scroll 28s linear infinite}}"
    inner = f'<g class="sc" transform="translate(0 0)"><g>{row}</g><g transform="translate({total} 0)">{row}</g><g transform="translate({total*2} 0)">{row}</g></g>'
    b = f'<text x="30" y="34" font-size="11" letter-spacing="3" font-weight="700" fill="{CY}">TOOLKIT</text>'
    b += f'<svg x="30" y="52" width="{w-60}" height="40" overflow="hidden"><g>{inner}</g></svg>'
    return wrap(w, h, b, css)

save("hero.svg", hero())
save("tile-focus.svg", tile("FOCUS", "◈", "Security", [("Ethical hacking", 70), ("Network security", 65), ("Linux security", 60)], CY, 0.2))
save("tile-build.svg", tile("BUILD", "⌘", "Projects", [("Python & Flask", 75), ("C", 60), ("Web / JS", 70)], GR, 0.5))
save("tile-learn.svg", tile("LEARN", "↗", "Next up", [("Cloud security", 45), ("AI for cyber defense", 50), ("Pentesting", 55)], PU, 0.8))
save("repo-core0.svg", repo("core0", "Autonomous cyber defense landing page.", "HTML", CY, 0.1, "WEB"))
save("repo-payguard.svg", repo("pay-guard", "A cost-aware credit-card fraud detector. Flags fraud and prices the mistakes in rupees.", "Jupyter Notebook", GR, 0.3, "ML"))
save("repo-malware-lab.svg", repo("malware-lifecycle-lab", "Local-only educational malware lifecycle lab: loopback C2, sandboxed ransomware simulation, Splunk detection.", "Python", PU, 0.5, "DEFENSE"))
save("repo-desktop-buddy.svg", repo("desktop-buddy", "Live pixel-art hometown wallpaper for Windows that mirrors your open apps.", "JavaScript", "#fbbf24", 0.7, "DESKTOP"))
save("stack.svg", stack())
print("ok")
