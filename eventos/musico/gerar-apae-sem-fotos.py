"""Arte do show da APAE (19/11/2026) sem fotos de pessoas: só grafismo e nomes."""
from PIL import Image, ImageDraw, ImageFont
import math, os

F = os.path.expanduser('~/.fonts/')
def font(n, s): return ImageFont.truetype(F + n, s)

BG = (20, 13, 8)
GOLD = (214, 160, 70)
CREAM = (242, 232, 214)
RED = (170, 38, 30)
GREEN = (30, 104, 58)
OCHRE = (196, 120, 40)
BLACK = (8, 6, 4)

def band(d, y, w, h):
    """Faixa geométrica de inspiração africana (blocos e zigue-zague)."""
    cols = [RED, GOLD, GREEN, GOLD, BLACK, OCHRE]
    bw = h
    for i, x in enumerate(range(0, w + bw, bw)):
        c = cols[i % len(cols)]
        d.rectangle([x, y, x + bw, y + h], fill=c)
        if c in (BLACK, GREEN, RED):
            d.polygon([(x, y + h), (x + bw / 2, y + h * 0.25), (x + bw, y + h)], fill=GOLD)
        else:
            d.polygon([(x, y), (x + bw / 2, y + h * 0.75), (x + bw, y)], fill=BLACK)
    d.line([0, y - 6, w, y - 6], fill=GOLD, width=3)
    d.line([0, y + h + 6, w, y + h + 6], fill=GOLD, width=3)

def sol(d, cx, cy, r):
    """Sol/tambor em círculos concêntricos com raios — símbolo abstrato, sem rosto."""
    for k in range(36):
        a = k * math.pi / 18
        r1, r2 = r * 1.08, r * (1.32 if k % 2 == 0 else 1.2)
        p = [(cx + r1 * math.cos(a - 0.05), cy + r1 * math.sin(a - 0.05)),
             (cx + r2 * math.cos(a), cy + r2 * math.sin(a)),
             (cx + r1 * math.cos(a + 0.05), cy + r1 * math.sin(a + 0.05))]
        d.polygon(p, fill=GOLD)
    for rr, c in [(r, GOLD), (r * 0.86, BG), (r * 0.78, RED), (r * 0.62, BG), (r * 0.54, GREEN), (r * 0.38, BG), (r * 0.30, GOLD)]:
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=c)
    for k in range(12):
        a = k * math.pi / 6
        x, y = cx + r * 0.70 * math.cos(a), cy + r * 0.70 * math.sin(a)
        d.ellipse([x - r * 0.035, y - r * 0.035, x + r * 0.035, y + r * 0.035], fill=GOLD)

def centro(d, y, txt, f, c, w, sp=0):
    if sp:
        widths = [d.textlength(ch, font=f) for ch in txt]
        tot = sum(widths) + sp * (len(txt) - 1)
        x = (w - tot) / 2
        for ch, cw in zip(txt, widths):
            d.text((x, y), ch, font=f, fill=c, features=['lnum'])
            x += cw + sp
    else:
        cormorant = 'Cormorant' in f.path
        t = txt.replace('ê', 'e') if cormorant else txt  # o ê convertido da Cormorant vem quebrado
        tw = d.textlength(t, font=f)
        x0 = (w - tw) / 2
        d.text((x0, y), t, font=f, fill=c, features=['lnum'])
        if cormorant:
            for i, ch in enumerate(txt):
                if ch == 'ê':
                    xe = x0 + d.textlength(t[:i], font=f)
                    l, top, r_, _ = f.getbbox('e')
                    cx = xe + (l + r_) / 2
                    sz = f.size
                    yb = y + top - sz * 0.06
                    d.line([(cx - sz * 0.11, yb), (cx, yb - sz * 0.13), (cx + sz * 0.11, yb)],
                           fill=c, width=max(2, int(sz * 0.045)), joint='curve')

def arte(w, h, saida):
    im = Image.new('RGB', (w, h), BG)
    d = ImageDraw.Draw(im)
    s = w / 1080
    bh = int(70 * s)
    band(d, int(40 * s), w, bh)
    band(d, h - int(40 * s) - bh, w, bh)
    story = h > 1500
    y = int((230 if story else 165) * s)
    centro(d, y, 'SHOW ESPECIAL', font('Montserrat-SemiBold.ttf', int(34 * s)), GOLD, w, sp=int(10 * s))
    y += int(70 * s)
    centro(d, y, 'Semana da', font('CormorantGaramond-MediumItalic.ttf', int(84 * s)), CREAM, w)
    y += int(92 * s)
    centro(d, y, 'Consciência Negra', font('CormorantGaramond-SemiBold.ttf', int(112 * s)), GOLD, w)
    y += int(150 * s)
    centro(d, y, 'MÚSICA · CULTURA · IDENTIDADE · RESISTÊNCIA', font('Montserrat-Medium.ttf', int(26 * s)), CREAM, w, sp=int(3 * s))
    r = int((190 if story else 95) * s)
    cy = y + int((330 if story else 190) * s)
    sol(d, w / 2, cy, r)
    y = cy + int(r * 1.32 + (90 if story else 40) * s)
    nf = int((96 if story else 84) * s)
    centro(d, y, 'Léa Soares', font('CormorantGaramond-SemiBold.ttf', nf), CREAM, w)
    y += int(nf * 1.02)
    centro(d, y, '&', font('CormorantGaramond-MediumItalic.ttf', int(nf * 0.66)), GOLD, w)
    y += int(nf * 0.72)
    centro(d, y, 'Abnadaby Bonaparte', font('CormorantGaramond-SemiBold.ttf', nf), CREAM, w)
    y += int(nf * 1.45)
    pass  # sem fio: cortava as letras de 'Abnadaby'
    centro(d, y, 'HOJE · 19/11 · 10H · APAE', font('Montserrat-SemiBold.ttf', int(44 * s)), GOLD, w, sp=int(4 * s))
    y += int(72 * s)
    centro(d, y, 'Em homenagem à Semana da Consciência Negra', font('Montserrat-Regular.ttf', int(28 * s)), CREAM, w)
    im.save(saida, quality=92)

base = os.path.dirname(os.path.abspath(__file__))
arte(1080, 1920, os.path.join(base, '2026-11-19-apae-sem-fotos-story.jpg'))
arte(1080, 1350, os.path.join(base, '2026-11-19-apae-sem-fotos-feed.jpg'))
