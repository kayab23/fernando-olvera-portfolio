from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.colors import HexColor
from datetime import datetime
import os

def create_cover_letter():
    """Genera carta de presentación profesional en PDF"""
    
    # Configuración del documento
    filename = "exports/Carta_Presentacion_Fernando_Olvera.pdf"
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )
    
    # Estilos
    styles = getSampleStyleSheet()
    
    # Estilo para nombre
    name_style = ParagraphStyle(
        'NameStyle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=HexColor('#2C3E50'),
        spaceAfter=4,
        alignment=TA_LEFT,
        fontName='Helvetica-Bold'
    )
    
    # Estilo para título profesional
    title_style = ParagraphStyle(
        'TitleStyle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=HexColor('#34495E'),
        spaceAfter=10,
        alignment=TA_LEFT,
        fontName='Helvetica'
    )
    
    # Estilo para información de contacto
    contact_style = ParagraphStyle(
        'ContactStyle',
        parent=styles['Normal'],
        fontSize=9,
        textColor=HexColor('#7F8C8D'),
        spaceAfter=20,
        alignment=TA_LEFT,
        fontName='Helvetica',
        leading=12
    )
    
    # Estilo para fecha y destinatario
    date_style = ParagraphStyle(
        'DateStyle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=HexColor('#2C3E50'),
        spaceAfter=8,
        alignment=TA_LEFT,
        fontName='Helvetica'
    )
    
    # Estilo para saludo
    greeting_style = ParagraphStyle(
        'GreetingStyle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=HexColor('#2C3E50'),
        spaceAfter=12,
        alignment=TA_LEFT,
        fontName='Helvetica-Bold'
    )
    
    # Estilo para cuerpo de la carta
    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=HexColor('#2C3E50'),
        spaceAfter=12,
        alignment=TA_JUSTIFY,
        fontName='Helvetica',
        leading=16
    )
    
    # Estilo para cierre
    closing_style = ParagraphStyle(
        'ClosingStyle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=HexColor('#2C3E50'),
        spaceAfter=30,
        alignment=TA_LEFT,
        fontName='Helvetica'
    )
    
    # Estilo para firma
    signature_style = ParagraphStyle(
        'SignatureStyle',
        parent=styles['Normal'],
        fontSize=11,
        textColor=HexColor('#2C3E50'),
        spaceAfter=4,
        alignment=TA_LEFT,
        fontName='Helvetica-Bold'
    )
    
    # Contenido del documento
    story = []
    
    # Encabezado con información personal
    story.append(Paragraph("Fernando Olvera Rendón", name_style))
    story.append(Paragraph("Analista de Datos | Especialista en Business Intelligence & Automatización", title_style))
    story.append(Paragraph(
        "Ciudad de México, México | +52 5583597359 | Tel. Fijo: 5593128401<br/>"
        "Kayab2309@gmail.com | <a href='https://linkedin.com/in/fernando-olvera-059739242' color='#3498DB'>LinkedIn</a> | "
        "<a href='https://fernando-olvera-portfolio.onrender.com' color='#3498DB'>Portfolio</a>",
        contact_style
    ))
    
    story.append(Spacer(1, 0.2*inch))
    
    # Fecha y destinatario
    fecha_actual = "26 de noviembre de 2025"
    story.append(Paragraph(fecha_actual, date_style))
    story.append(Paragraph("Departamento de Recursos Humanos / Gerente de Contratación", date_style))
    story.append(Paragraph("LEIDOS", date_style))
    story.append(Paragraph("Reston, Virginia, Estados Unidos", date_style))
    
    story.append(Spacer(1, 0.2*inch))
    
    # Saludo
    story.append(Paragraph("Estimado(a) Gerente de Contratación de LEIDOS:", greeting_style))
    
    # Párrafo 1: Introducción impactante
    story.append(Paragraph(
        "Con más de <b>6 años de experiencia transformando datos en decisiones estratégicas</b> y un historial comprobado "
        "de generación de impacto medible en empresas Fortune 500 como <b>Procter & Gamble</b> y líderes del sector como "
        "<b>Glidewell Dental</b>, me dirijo a ustedes con gran interés en contribuir al éxito de <b>LEIDOS</b> como "
        "<b>Analista de Datos</b> y <b>Desarrollador</b>. Mi combinación única de expertise técnico en Python, SQL, Power BI "
        "y desarrollo de software, junto con mi capacidad demostrada para automatizar procesos y crear soluciones innovadoras, "
        "me posiciona como el candidato ideal para apoyar la misión de LEIDOS en la transformación digital y el análisis de "
        "datos críticos para la defensa y seguridad nacional.",
        body_style
    ))
    
    # Párrafo 2: Experiencia y logros cuantificables
    story.append(Paragraph(
        "Durante mi trayectoria profesional, he liderado proyectos que han generado resultados excepcionales: desarrollé un "
        "<b>sistema GPS en tiempo real</b> para representantes de ventas que mejoró la productividad del equipo en un 30%; "
        "creé dashboards en Power BI para el sector automotriz que incrementaron la visibilidad operativa en un 22%; "
        "e implementé un sistema de análisis comercial con Machine Learning que aumentó el performance del equipo en 28%. "
        "Estos logros reflejan mi capacidad para traducir requerimientos de negocio en soluciones tecnológicas escalables "
        "que generan valor real.",
        body_style
    ))
    
    # Párrafo 3: Habilidades técnicas específicas
    story.append(Paragraph(
        "Mi dominio técnico abarca el stack completo de análisis de datos: desde la <b>extracción y transformación de datos</b> "
        "utilizando Python (Pandas, NumPy) y SQL complejos, hasta la creación de <b>dashboards interactivos</b> en Power BI y "
        "Tableau con DAX avanzado y visualizaciones personalizadas. Poseo experiencia práctica en el <b>desarrollo de aplicaciones "
        "web progresivas (PWA)</b> con Flask, WebSocket y APIs RESTful, así como en la implementación de <b>procesos ETL</b> "
        "robustos que aseguran la calidad y confiabilidad de los datos. Además, cuento con conocimientos en <b>Machine Learning</b>, "
        "análisis predictivo y servicios de nube AWS, lo que me permite abordar desafíos complejos con soluciones innovadoras.",
        body_style
    ))
    
    # Párrafo 4: Automatización y eficiencia
    story.append(Paragraph(
        "Uno de mis mayores aportes ha sido la <b>automatización estratégica de procesos</b>. En Glidewell, automaticé el envío "
        "diario de informes en PDF y Excel, eliminando tareas manuales y asegurando entregas puntuales; desarrollé un sistema "
        "de gestión de casos dentales que centralizó la captura y seguimiento de datos de producción; y creé reportes automatizados "
        "que redujeron en un <b>80% el tiempo dedicado a reportería manual</b>. Esta orientación a la eficiencia no solo libera "
        "tiempo valioso del equipo, sino que también garantiza la precisión y consistencia de la información crítica para la "
        "toma de decisiones.",
        body_style
    ))
    
    # Párrafo 5: Experiencia en empresas reconocidas
    story.append(Paragraph(
        "Mi experiencia de <b>9 años en Procter & Gamble</b>, empresa Fortune 500, me proporcionó una base sólida en control "
        "de calidad, gestión de equipos y generación de reportes gerenciales en entornos de alta exigencia. Esta experiencia, "
        "combinada con mis roles recientes como Analista de Datos en empresas tecnológicas y de servicios, me ha permitido "
        "desarrollar una perspectiva integral del ciclo de vida de los datos: desde su captura y limpieza hasta su transformación "
        "en insights accionables que impulsan estrategias de negocio.",
        body_style
    ))
    
    # Párrafo 6: Proyectos verificables y código abierto
    story.append(Paragraph(
        "Todos mis proyectos están respaldados por <b>código público verificable en GitHub</b> (github.com/kayab23), incluyendo "
        "el sistema FTA Dashboard con más de 98 commits, sistema de alertas de visitas, generador automatizado de reportes, y el "
        "proyecto Call Center Analytics con más de 3,500 líneas de código Python. Mi portfolio online "
        "(fernando-olvera-portfolio.onrender.com) presenta documentación técnica completa, arquitecturas detalladas y resultados "
        "medibles de cada proyecto, demostrando mi compromiso con la <b>transparencia, calidad del código y mejores prácticas</b> "
        "de desarrollo.",
        body_style
    ))
    
    # Párrafo 7: Habilidades blandas y valor agregado
    story.append(Paragraph(
        "Más allá de mis habilidades técnicas, aporto una <b>orientación a resultados</b> que se refleja en cada proyecto que "
        "emprendo. Mi capacidad de <b>comunicación efectiva</b> me permite traducir conceptos técnicos complejos en insights "
        "comprensibles para stakeholders no técnicos. Mi <b>pensamiento analítico</b> y habilidad para la <b>resolución de "
        "problemas</b> me permiten identificar patrones ocultos en los datos y proponer soluciones innovadoras. Soy un profesional "
        "en <b>aprendizaje continuo</b>, certificado por Google como Analista de Datos, con formación adicional en Python para "
        "Ciencia de Datos y múltiples certificaciones técnicas que demuestran mi compromiso con la excelencia profesional.",
        body_style
    ))
    
    # Párrafo 8: Cierre y llamado a la acción
    story.append(Paragraph(
        "Estoy convencido de que mi combinación de experiencia técnica profunda, habilidad para desarrollar soluciones completas "
        "de software, y mi historial comprobado de generación de valor medible, me convierten en el candidato ideal para el equipo "
        "de <b>LEIDOS</b>. Me entusiasma la oportunidad de contribuir a la misión de LEIDOS en la aplicación de tecnología avanzada "
        "para resolver desafíos críticos, aplicando mi expertise en análisis de datos, desarrollo de aplicaciones y automatización "
        "de procesos en proyectos de alto impacto. <b>Estoy disponible para una entrevista</b> en el momento que consideren "
        "conveniente para discutir cómo puedo aportar valor inmediato a sus objetivos estratégicos.",
        body_style
    ))
    
    # Cierre
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Atentamente,", closing_style))
    
    # Firma
    story.append(Paragraph("Fernando Olvera Rendón", signature_style))
    story.append(Paragraph("Analista de Datos | Desarrollador", title_style))
    
    # Generar PDF
    doc.build(story)
    print(f"✅ Carta de presentación generada exitosamente: {filename}")
    print(f"📄 Tamaño del archivo: {os.path.getsize(filename) / 1024:.1f} KB")

if __name__ == "__main__":
    create_cover_letter()
