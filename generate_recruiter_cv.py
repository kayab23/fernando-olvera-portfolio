import markdown
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
import re

def generate_recruiter_cv():
    """Generar CV optimizado para reclutadores con formato profesional"""
    
    # Leer el archivo markdown
    with open('CV_Fernando_Olvera.md', 'r', encoding='utf-8') as file:
        md_content = file.read()
    
    # Crear PDF
    pdf_path = 'exports/CV_Fernando_Olvera_RECLUTADORES.pdf'
    doc = SimpleDocTemplate(pdf_path, pagesize=A4, 
                          rightMargin=50, leftMargin=50,
                          topMargin=50, bottomMargin=50)
    
    # Estilos profesionales
    styles = getSampleStyleSheet()
    
    # Estilo para el título principal
    title_style = ParagraphStyle(
        'MainTitle',
        parent=styles['Heading1'],
        fontSize=26,
        spaceAfter=8,
        textColor=HexColor('#1a365d'),
        alignment=1,  # Centro
        fontName='Helvetica-Bold'
    )
    
    # Estilo para subtítulo profesional
    subtitle_style = ParagraphStyle(
        'ProfessionalSubtitle',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=15,
        textColor=HexColor('#2d5aa0'),
        alignment=1,  # Centro
        fontName='Helvetica-Bold'
    )
    
    # Estilo para información de contacto
    contact_style = ParagraphStyle(
        'ContactInfo',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=4,
        alignment=1,  # Centro
        textColor=HexColor('#2c5282'),
        fontName='Helvetica'
    )
    
    # Estilo para secciones principales
    section_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Heading2'],
        fontSize=14,
        spaceBefore=20,
        spaceAfter=10,
        textColor=HexColor('#1a365d'),
        borderWidth=2,
        borderColor=HexColor('#2d5aa0'),
        borderPadding=(8, 5, 8, 5),
        leftIndent=0,
        fontName='Helvetica-Bold',
        backColor=HexColor('#f7fafc')
    )
    
    # Estilo para experiencia laboral
    job_title_style = ParagraphStyle(
        'JobTitle',
        parent=styles['Heading3'],
        fontSize=12,
        spaceBefore=15,
        spaceAfter=8,
        textColor=HexColor('#2d5aa0'),
        fontName='Helvetica-Bold'
    )
    
    # Estilo para habilidades técnicas
    skill_style = ParagraphStyle(
        'SkillItem',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=6,
        leftIndent=20,
        fontName='Helvetica'
    )
    
    # Procesar contenido
    story = []
    lines = md_content.split('\n')
    
    i = 0
    in_table = False
    table_data = []
    
    while i < len(lines):
        line = lines[i].strip()
        
        if line.startswith('# '):
            # Título principal
            title = line[2:].strip()
            story.append(Paragraph(title, title_style))
            story.append(Spacer(1, 8))
            
        elif line.startswith('### ') and 'Analista de Datos' in line:
            # Subtítulo profesional
            subtitle = line[4:].strip()
            story.append(Paragraph(subtitle, subtitle_style))
            story.append(Spacer(1, 15))
            
        elif line.startswith('**📧') or line.startswith('**📱') or line.startswith('**📍') or line.startswith('**💼') or line.startswith('**🌐'):
            # Información de contacto
            clean_line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
            clean_line = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" color="blue">\1</a>', clean_line)
            story.append(Paragraph(clean_line, contact_style))
            
        elif line.startswith('| ') and '|' in line:
            # Procesar tabla de habilidades técnicas
            if not in_table:
                in_table = True
                table_data = []
            
            if 'Tecnología' in line and 'Nivel' in line:
                # Encabezado de habilidades técnicas
                skills_title = "🛠️ Habilidades Técnicas"
                story.append(Paragraph(skills_title, section_style))
                story.append(Spacer(1, 10))
            else:
                # Fila de datos
                cells = [cell.strip() for cell in line.split('|')[1:-1]]
                if len(cells) >= 2 and cells[0] and cells[1]:
                    tech = cells[0].replace('**', '')
                    level = cells[1].replace('█', '●').replace('%', '%')
                    table_data.append([tech, level])
        
        elif in_table and (not line or not line.startswith('|')):
            # Fin de tabla - procesar habilidades
            if table_data:
                for tech, level in table_data:
                    skill_text = f"<b>{tech}:</b> {level}"
                    story.append(Paragraph(skill_text, skill_style))
                story.append(Spacer(1, 15))
            in_table = False
            table_data = []
            
            # Procesar línea actual
            if line and not line.startswith('---'):
                if line.startswith('### '):
                    section_title = line[4:].strip()
                    story.append(Paragraph(section_title, section_style))
                    story.append(Spacer(1, 10))
                elif line.startswith('#### '):
                    job_info = line[5:].strip()
                    story.append(Paragraph(job_info, job_title_style))
                elif line.startswith('- '):
                    item = line[2:].strip()
                    clean_item = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', item)
                    story.append(Paragraph(f"• {clean_item}", styles['Normal']))
                elif line:
                    clean_line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
                    clean_line = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" color="blue">\1</a>', clean_line)
                    story.append(Paragraph(clean_line, styles['Normal']))
                    story.append(Spacer(1, 6))
            
        elif line.startswith('### '):
            # Secciones principales
            section_title = line[4:].strip()
            story.append(Paragraph(section_title, section_style))
            story.append(Spacer(1, 10))
            
        elif line.startswith('#### '):
            # Subsecciones (trabajos)
            job_info = line[5:].strip()
            story.append(Paragraph(job_info, job_title_style))
            
        elif line.startswith('- '):
            # Listas
            item = line[2:].strip()
            clean_item = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', item)
            clean_item = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" color="blue">\1</a>', clean_item)
            story.append(Paragraph(f"• {clean_item}", styles['Normal']))
            
        elif line and not line.startswith('---'):
            # Texto normal
            if line:
                clean_line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
                clean_line = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" color="blue">\1</a>', clean_line)
                story.append(Paragraph(clean_line, styles['Normal']))
                story.append(Spacer(1, 6))
        
        i += 1
    
    # Procesar tabla final si existe
    if in_table and table_data:
        for tech, level in table_data:
            skill_text = f"<b>{tech}:</b> {level}"
            story.append(Paragraph(skill_text, skill_style))
    
    # Construir PDF
    doc.build(story)
    
    print(f"✅ CV para RECLUTADORES generado: {pdf_path}")
    print(f"🎯 Optimizado para: Impresión profesional y entrevistas")
    print(f"📧 Email: Kayab2309@gmail.com")
    print(f"🌐 Portfolio: https://fernando-olvera-portfolio.onrender.com")
    return pdf_path

if __name__ == "__main__":
    try:
        cv_file = generate_recruiter_cv()
        print(f"📄 CV listo para entregar a reclutadores: {cv_file}")
        print("🖨️ Listo para imprimir en formato profesional")
    except Exception as e:
        print(f"❌ Error: {e}")