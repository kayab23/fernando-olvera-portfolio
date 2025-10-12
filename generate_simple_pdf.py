import markdown
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
import re

def markdown_to_pdf_simple():
    """Convierte markdown a PDF usando ReportLab"""
    
    # Leer el archivo markdown
    with open('CV_Fernando_Olvera.md', 'r', encoding='utf-8') as file:
        md_content = file.read()
    
    # Crear PDF
    pdf_path = 'exports/cv_fernando_olvera_with_portfolio.pdf'
    doc = SimpleDocTemplate(pdf_path, pagesize=A4, 
                          rightMargin=72, leftMargin=72,
                          topMargin=72, bottomMargin=18)
    
    # Estilos
    styles = getSampleStyleSheet()
    
    # Estilo personalizado para el título
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=6,
        textColor=HexColor('#2c3e50'),
        alignment=1,  # Centro
    )
    
    # Estilo para subtítulos
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=12,
        textColor=HexColor('#3498db'),
        alignment=1,  # Centro
    )
    
    # Estilo para información de contacto
    contact_style = ParagraphStyle(
        'ContactInfo',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=6,
        alignment=1,  # Centro
        textColor=HexColor('#34495e'),
    )
    
    # Estilo para secciones
    section_style = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading2'],
        fontSize=16,
        spaceBefore=20,
        spaceAfter=12,
        textColor=HexColor('#2c3e50'),
        borderWidth=1,
        borderColor=HexColor('#3498db'),
        borderPadding=5,
        leftIndent=10,
    )
    
    # Procesar contenido
    story = []
    lines = md_content.split('\n')
    
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        
        if line.startswith('# '):
            # Título principal
            title = line[2:].strip()
            story.append(Paragraph(title, title_style))
            story.append(Spacer(1, 6))
            
        elif line.startswith('### ') and 'Analista de Datos' in line:
            # Subtítulo
            subtitle = line[4:].strip()
            story.append(Paragraph(subtitle, subtitle_style))
            story.append(Spacer(1, 12))
            
        elif line.startswith('**📧') or line.startswith('**📱') or line.startswith('**📍') or line.startswith('**💼') or line.startswith('**🌐'):
            # Información de contacto
            # Limpiar markdown básico
            clean_line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
            clean_line = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', clean_line)
            story.append(Paragraph(clean_line, contact_style))
            
        elif line.startswith('### 🎯'):
            # Sección de perfil
            story.append(Spacer(1, 12))
            section_title = line[4:].strip()
            story.append(Paragraph(section_title, section_style))
            
        elif line.startswith('### '):
            # Otras secciones
            story.append(Spacer(1, 12))
            section_title = line[4:].strip()
            story.append(Paragraph(section_title, section_style))
            
        elif line.startswith('#### '):
            # Subsecciones (experiencia laboral)
            subsection = line[5:].strip()
            subsection_style = ParagraphStyle(
                'Subsection',
                parent=styles['Heading3'],
                fontSize=12,
                spaceBefore=12,
                spaceAfter=6,
                textColor=HexColor('#2980b9'),
            )
            story.append(Paragraph(subsection, subsection_style))
            
        elif line.startswith('- '):
            # Lista de elementos
            item = line[2:].strip()
            # Limpiar markdown básico
            clean_item = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', item)
            clean_item = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', clean_item)
            story.append(Paragraph(f"• {clean_item}", styles['Normal']))
            
        elif line and not line.startswith('---') and not line.startswith('|'):
            # Texto normal
            if line:
                # Limpiar markdown básico
                clean_line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
                clean_line = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', clean_line)
                story.append(Paragraph(clean_line, styles['Normal']))
                story.append(Spacer(1, 6))
        
        i += 1
    
    # Construir PDF
    doc.build(story)
    
    print(f"✅ PDF generado exitosamente: {pdf_path}")
    print(f"🌐 Incluye link del portfolio: https://fernando-olvera-portfolio.onrender.com")
    return pdf_path

if __name__ == "__main__":
    try:
        pdf_file = markdown_to_pdf_simple()
        print(f"📄 Archivo PDF listo para envío: {pdf_file}")
    except Exception as e:
        print(f"❌ Error: {e}")