from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from pathlib import Path

ASSETS_DIR = Path("website-portfolio/assets")

items = [
    ("BMW - Esquema y Dispersion.pdf", "BMW - Esquema y Dispersion"),
    ("DasPresu.pdf", "DasPresu"),
    ("cubo.pdf", "cubo"),
]

def make_placeholder(path: Path, title: str):
    c = canvas.Canvas(str(path), pagesize=A4)
    w, h = A4
    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(w/2, h - 60, title)
    c.setFont("Helvetica", 12)
    c.drawCentredString(w/2, h - 80, "Placeholder PDF — vista previa generada automáticamente")

    margin = 40 * mm
    box_w = w - margin * 2
    box_h = h/2
    box_x = margin
    box_y = h - 140 - box_h
    c.setStrokeColorRGB(0.2, 0.2, 0.2)
    c.rect(box_x, box_y, box_w, box_h, stroke=1, fill=0)
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(box_x + 6*mm, box_y + 6*mm, "Aquí debería ir la miniatura del dashboard (SVG) o una captura real.")

    c.showPage()
    c.save()


def main():
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)
    for filename, title in items:
        out = ASSETS_DIR / filename
        print(f"Creating {out}")
        make_placeholder(out, title)

if __name__ == '__main__':
    main()
