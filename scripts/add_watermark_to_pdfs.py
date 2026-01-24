import os
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import Color
from io import BytesIO

# Configuración
CERTS_DIR = os.path.join('website-portfolio', 'assets', 'certs')
OUTPUT_DIR = os.path.join(CERTS_DIR, 'watermarked')
WATERMARK_TEXT = 'Fernando Olvera | kayab2309@gmail.com'

os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_watermark(text, page_size=letter):
    # Asegura que page_size sean floats
    width = float(page_size[0])
    height = float(page_size[1])
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=(width, height))
    can.saveState()
    can.setFont('Helvetica-Bold', 24)
    can.setFillColor(Color(0.5, 0.5, 0.5, alpha=0.25))
    can.translate(width/2, height/2)
    can.rotate(45)
    can.drawCentredString(0, 0, text)
    can.restoreState()
    can.save()
    packet.seek(0)
    return PdfReader(packet)

def add_watermark_to_pdf(input_pdf_path, output_pdf_path, watermark_text):
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()
    # Create watermark for the first page size
    watermark_pdf = create_watermark(watermark_text, reader.pages[0].mediabox)
    watermark_page = watermark_pdf.pages[0]
    for page in reader.pages:
        # Recreate watermark if page size changes
        if (page.mediabox[2], page.mediabox[3]) != (watermark_page.mediabox[2], watermark_page.mediabox[3]):
            watermark_pdf = create_watermark(watermark_text, (float(page.mediabox[2]), float(page.mediabox[3])))
            watermark_page = watermark_pdf.pages[0]
        page.merge_page(watermark_page)
        writer.add_page(page)
    with open(output_pdf_path, 'wb') as f:
        writer.write(f)

def process_all_pdfs():
    for fname in os.listdir(CERTS_DIR):
        if fname.lower().endswith('.pdf'):
            in_path = os.path.join(CERTS_DIR, fname)
            out_path = os.path.join(OUTPUT_DIR, fname)
            print(f'Procesando: {fname}')
            add_watermark_to_pdf(in_path, out_path, WATERMARK_TEXT)
    print('Listo. PDFs con marca de agua en:', OUTPUT_DIR)

if __name__ == '__main__':
    process_all_pdfs()
