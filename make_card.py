#!/usr/bin/env python3
"""
Generate a printable A6-landscape Christmas card PDF with a QR code.

Usage:
  python make_card.py --url "https://YOUR.URL/...?name=Theresa" --to "Theresa" --out weihnachtsbillet.pdf
"""
import argparse
from pathlib import Path
import qrcode
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A6, landscape
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.colors import Color
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics

def draw_wrapped(c, text, x, y, max_width, font_name, font_size, leading=None):
    c.setFont(font_name, font_size)
    if leading is None:
        leading = font_size*1.25
    words = text.split()
    lines=[]
    cur=""
    for w in words:
        test = (cur+" "+w).strip()
        if pdfmetrics.stringWidth(test, font_name, font_size) <= max_width:
            cur=test
        else:
            if cur:
                lines.append(cur)
            cur=w
    if cur:
        lines.append(cur)
    for line in lines:
        c.drawString(x, y, line)
        y -= leading
    return y

def blob(c, x,y,r,alpha=0.12, col=Color(0.53,0.69,0.58)):
    c.saveState()
    try:
        c.setFillAlpha(alpha)
    except Exception:
        pass
    c.setFillColor(col)
    c.circle(x,y,r, stroke=0, fill=1)
    c.restoreState()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True, help="Target URL encoded in the QR code")
    ap.add_argument("--to", default="Theresa", help="Recipient name after 'Für:'")
    ap.add_argument("--out", default="weihnachtsbillet.pdf", help="Output PDF filename")
    args = ap.parse_args()

    # QR PNG in-memory
    qr_img = qrcode.make(args.url).resize((900,900), Image.NEAREST)

    out_path = Path(args.out)
    page_w, page_h = landscape(A6)
    c = canvas.Canvas(str(out_path), pagesize=landscape(A6))

    # background
    c.setFillColor(Color(0.97,0.96,0.93))
    c.rect(0,0,page_w,page_h, fill=1, stroke=0)
    blob(c, 42, page_h-28, 58, 0.18)
    blob(c, page_w-34, page_h-46, 76, 0.14)
    blob(c, page_w-52, 44, 86, 0.12)
    blob(c, 62, 34, 64, 0.10)

    margin = 16
    qr_side = 65*mm
    qr_x = page_w - margin - qr_side
    qr_y = (page_h - qr_side)/2
    left_max = qr_x - margin - 18

    c.setFillColor(Color(0.33,0.45,0.36))
    c.setFont("Helvetica-Bold", 24)
    c.drawString(margin, page_h-40, "Frohe Weihnachten!")

    c.setFillColor(colors.black)
    y = page_h-60
    y = draw_wrapped(c, "Scanne den QR-Code: Mini-Spiel → Gutschein wird freigeschaltet.", margin, y, left_max, "Helvetica", 11, leading=14)

    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, page_h-92, "Für:")
    c.setFont("Helvetica", 12)
    c.drawString(margin+34, page_h-92, args.to)

    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, page_h-114, "Von:")
    c.setFont("Helvetica", 12)
    c.line(margin+34, page_h-116, qr_x-18, page_h-116)

    c.setFont("Helvetica-Bold", 12)
    c.drawString(margin, page_h-150, "So funktioniert’s:")

    y = page_h-166
    for s in [
        "1) QR-Code scannen und Matcha-Whisk-Dash spielen.",
        "2) 15 Punkte in 30 Sekunden → Gutschein erscheint.",
        "3) Nach 3 Versuchen wird automatisch freigeschaltet."
    ]:
        y = draw_wrapped(c, s, margin, y, left_max, "Helvetica", 10.5, leading=13)
        y -= 1

    c.setFont("Helvetica-Oblique", 9.3)
    c.setFillColor(Color(0.16,0.16,0.16))
    c.drawString(margin, 20, "PS: Ton an den Händen ist okay. Matcha im Pulli weniger.")

    # QR card
    c.saveState()
    try:
        c.setFillAlpha(0.92)
    except Exception:
        pass
    c.setFillColor(colors.white)
    c.roundRect(qr_x-8, qr_y-8, qr_side+16, qr_side+34, 14, stroke=0, fill=1)
    c.restoreState()

    c.setStrokeColor(Color(0,0,0,0.12))
    c.roundRect(qr_x-8, qr_y-8, qr_side+16, qr_side+34, 14, stroke=1, fill=0)

    c.setFont("Helvetica-Bold", 11)
    c.setFillColor(Color(0.33,0.45,0.36))
    c.drawCentredString(qr_x+qr_side/2, qr_y+qr_side+16, "Zum Spiel")

    c.drawImage(ImageReader(qr_img), qr_x, qr_y, width=qr_side, height=qr_side, mask='auto')

    c.setFont("Helvetica", 7.5)
    c.setFillColor(Color(0.25,0.25,0.25))
    c.drawCentredString(qr_x+qr_side/2, qr_y-6, "QR-Link: " + (args.url[:38] + ("…" if len(args.url)>38 else "")))

    c.showPage()
    c.save()
    print(f"Saved: {out_path.resolve()}")

if __name__ == "__main__":
    main()
