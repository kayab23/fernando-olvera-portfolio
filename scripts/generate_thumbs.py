#!/usr/bin/env python3
"""
Genera miniaturas (JPEG) de la primera página de cada PDF en
website-portfolio/assets/certs/ y las guarda en website-portfolio/assets/certs/thumbs/

Requiere: pymupdf (pip install pymupdf)

Uso:
    python scripts/generate_thumbs.py
"""
from pathlib import Path
import sys

BASE = Path(__file__).resolve().parents[1] / 'website-portfolio' / 'assets' / 'certs'
OUT = BASE / 'thumbs'
OUT.mkdir(parents=True, exist_ok=True)

def generate(pdf_path: Path, out_path: Path, width: int = 600):
    try:
        import fitz  # PyMuPDF
    except Exception as e:
        print("PyMuPDF no disponible. Instala con: pip install pymupdf")
        raise

    doc = fitz.open(str(pdf_path))
    page = doc.load_page(0)
    mat = fitz.Matrix(width / page.rect.width, width / page.rect.width)
    pix = page.get_pixmap(matrix=mat, alpha=False)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    pix.save(str(out_path))

def main():
    pdfs = sorted([p for p in BASE.iterdir() if p.suffix.lower() == '.pdf'])
    if not pdfs:
        print("No se encontraron PDFs en", BASE)
        return

    for pdf in pdfs:
        name = pdf.stem + '.jpg'
        out = OUT / name
        try:
            generate(pdf, out)
            print(f"Generada miniatura: {out}")
        except Exception as e:
            print(f"ERROR al procesar {pdf}: {e}")

if __name__ == '__main__':
    main()
