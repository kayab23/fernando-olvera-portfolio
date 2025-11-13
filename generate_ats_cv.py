import markdown
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT, TA_CENTER
import re
import os

def generate_ats_cv():
    """Generar CV optimizado para ATS (Applicant Tracking Systems)"""
    
    # Leer el archivo markdown optimizado para ATS
    with open('CV_Fernando_Olvera_ATS.md', 'r', encoding='utf-8') as file:
        md_content = file.read()
    
    # Crear PDF
    pdf_path = 'exports/CV. Fernando Olvera.pdf'
    doc = SimpleDocTemplate(pdf_path, pagesize=A4, 
                          rightMargin=60, leftMargin=60,
                          topMargin=60, bottomMargin=60)
    
    # Estilos optimizados para ATS - fuentes estándar y formato simple
    styles = getSampleStyleSheet()
    
    # Estilo para el nombre (título principal)
    name_style = ParagraphStyle(
        'Name',
        parent=styles['Heading1'],
        fontSize=20,
        spaceAfter=4,
        textColor=HexColor('#000000'),
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    # Estilo para el título profesional
    title_style = ParagraphStyle(
        'ProfessionalTitle',
        parent=styles['Heading2'],
        fontSize=14,
        spaceAfter=12,
        textColor=HexColor('#000000'),
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    # Estilo para información de contacto
    contact_style = ParagraphStyle(
        'ContactInfo',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=3,
        alignment=TA_LEFT,
        textColor=HexColor('#000000'),
        fontName='Helvetica'
    )
    
    # Estilo para secciones principales - ATS-friendly
    section_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Heading2'],
        fontSize=12,
        spaceBefore=16,
        spaceAfter=8,
        textColor=HexColor('#000000'),
        fontName='Helvetica-Bold',
        leftIndent=0
    )
    
    # Estilo para subsecciones (títulos de trabajo)
    subsection_style = ParagraphStyle(
        'Subsection',
        parent=styles['Heading3'],
        fontSize=11,
        spaceBefore=10,
        spaceAfter=5,
        textColor=HexColor('#000000'),
        fontName='Helvetica-Bold'
    )
    
    # Estilo para texto normal
    normal_style = ParagraphStyle(
        'NormalText',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=4,
        textColor=HexColor('#000000'),
        fontName='Helvetica',
        leading=14
    )
    
    # Estilo para bullets
    bullet_style = ParagraphStyle(
        'BulletText',
        parent=styles['Normal'],
        fontSize=10,
        spaceAfter=4,
        leftIndent=20,
        textColor=HexColor('#000000'),
        fontName='Helvetica',
        leading=14
    )
    
    # Procesar contenido
    story = []
    lines = md_content.split('\n')
    
    i = 0
    skip_next_lines = 0
    header_added = False
    
    while i < len(lines):
        if skip_next_lines > 0:
            skip_next_lines -= 1
            i += 1
            continue
            
        line = lines[i].strip()
        
        # Título principal (nombre) - crear encabezado con foto
        if line.startswith('# ') and i < 3 and not header_added:
            name = line[2:].strip()
            
            # Buscar título profesional y datos de contacto
            prof_title = ""
            contact_lines = []
            
            for j in range(i+1, min(i+15, len(lines))):
                temp_line = lines[j].strip()
                if temp_line.startswith('## ') and j < 5:
                    prof_title = temp_line[3:].strip()
                elif temp_line.startswith('**Email:**') or temp_line.startswith('**Teléfono:**') or \
                     temp_line.startswith('**Ubicación:**') or temp_line.startswith('**LinkedIn:**') or \
                     temp_line.startswith('**Portfolio:**'):
                    clean_temp = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', temp_line)
                    clean_temp = re.sub(r'\[(.*?)\]\((.*?)\)', r'\1', clean_temp)
                    contact_lines.append(clean_temp)
            
            # Crear columna izquierda con texto
            left_content = []
            left_content.append(Paragraph(name, name_style))
            if prof_title:
                left_content.append(Spacer(1, 4))
                left_content.append(Paragraph(prof_title, title_style))
            
            left_content.append(Spacer(1, 8))
            for contact_line in contact_lines:
                left_content.append(Paragraph(contact_line, contact_style))
            
            # Intentar cargar foto
            foto_path = 'assets/foto.jpeg'
            if os.path.exists(foto_path):
                try:
                    foto = Image(foto_path, width=1.5*inch, height=1.5*inch)
                    
                    # Crear tabla: texto izquierda, foto derecha
                    header_table = Table([[left_content, foto]], 
                                        colWidths=[4.5*inch, 2*inch])
                    header_table.setStyle(TableStyle([
                        ('ALIGN', (0, 0), (0, 0), 'LEFT'),
                        ('ALIGN', (1, 0), (1, 0), 'RIGHT'),
                        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                        ('LEFTPADDING', (0, 0), (-1, -1), 0),
                        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                        ('TOPPADDING', (0, 0), (-1, -1), 0),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 15),
                    ]))
                    
                    story.append(header_table)
                    header_added = True
                    
                    # Saltar las líneas procesadas
                    skip_next_lines = len(contact_lines) + 3
                    
                except Exception as e:
                    print(f"⚠️ Error cargando foto: {e}")
                    # Fallback sin foto
                    for item in left_content:
                        story.append(item)
                    story.append(Spacer(1, 15))
                    header_added = True
            else:
                print(f"⚠️ Foto no encontrada: {foto_path}")
                # Fallback sin foto
                for item in left_content:
                    story.append(item)
                story.append(Spacer(1, 15))
                header_added = True
            
        # Saltar título profesional y contacto si ya se procesaron en el header
        elif (line.startswith('## ') and i < 5) or \
             (line.startswith('**Email:**') or line.startswith('**Teléfono:**') or \
              line.startswith('**Ubicación:**') or line.startswith('**LinkedIn:**') or \
              line.startswith('**Portfolio:**')) and not header_added:
            pass  # Ya procesado en el header
            
        # Separadores ---
        elif line.startswith('---'):
            if story:  # Solo agregar espaciador si ya hay contenido
                story.append(Spacer(1, 8))
            
        # Secciones principales
        elif line.startswith('## ') and i >= 5:
            section = line[3:].strip()
            story.append(Spacer(1, 4))
            story.append(Paragraph(section, section_style))
            
        # Subsecciones (títulos de trabajo con ###)
        elif line.startswith('### '):
            subsection = line[4:].strip()
            story.append(Paragraph(subsection, subsection_style))
            
        # Bullets
        elif line.startswith('- '):
            item = line[2:].strip()
            # Limpiar markdown pero mantener negritas para palabras clave
            clean_item = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', item)
            clean_item = re.sub(r'\[(.*?)\]\((.*?)\)', r'\1', clean_item)
            story.append(Paragraph(f"• {clean_item}", bullet_style))
            
        # Texto normal
        elif line and not line.startswith('#') and not line.startswith('**Tecnologías:**') \
             and not line.startswith('**Logros'):
            clean_line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
            clean_line = re.sub(r'\[(.*?)\]\((.*?)\)', r'\1', clean_line)
            
            # Si es una línea de tecnologías o logros clave
            if 'Tecnologías:' in line or 'Logros clave:' in line or 'GitHub:' in line:
                story.append(Paragraph(clean_line, bullet_style))
            else:
                story.append(Paragraph(clean_line, normal_style))
        
        i += 1
    
    # Construir PDF
    doc.build(story)
    
    print(f"✅ CV OPTIMIZADO PARA ATS generado: {pdf_path}")
    print(f"🎯 Características ATS-friendly:")
    print(f"   • Fuentes estándar (Helvetica)")
    print(f"   • Formato simple sin tablas complejas")
    print(f"   • Palabras clave resaltadas")
    print(f"   • Estructura jerárquica clara")
    print(f"   • Secciones bien definidas")
    print(f"\n📧 Email: Kayab2309@gmail.com")
    print(f"🌐 Portfolio: https://fernando-olvera-portfolio.onrender.com")
    return pdf_path

if __name__ == "__main__":
    try:
        cv_file = generate_ats_cv()
        print(f"\n📄 CV listo para sistemas ATS: {cv_file}")
        print("🤖 Optimizado para parsing automático por reclutadores")
        print("\n💡 Palabras clave incluidas:")
        print("   ETL, SQL, Python, Power BI, Tableau, Machine Learning,")
        print("   AWS, Big Data, Business Intelligence, Dashboards, APIs,")
        print("   Automatización, Data Analytics, KPIs, y más...")
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
