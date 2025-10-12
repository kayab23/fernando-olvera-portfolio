import markdown
from weasyprint import HTML, CSS
from pathlib import Path

# Leer el archivo markdown actualizado
with open('CV_Fernando_Olvera.md', 'r', encoding='utf-8') as file:
    md_content = file.read()

# Convertir markdown a HTML
html_content = markdown.markdown(md_content, extensions=['tables'])

# CSS mejorado para el CV
css_content = """
@page {
    size: A4;
    margin: 1.5cm;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    color: #333;
    max-width: 800px;
    margin: 0 auto;
}

h1 {
    color: #2c3e50;
    border-bottom: 3px solid #3498db;
    padding-bottom: 10px;
    margin-bottom: 5px;
}

h3 {
    color: #3498db;
    font-style: italic;
    margin-top: 0;
    margin-bottom: 20px;
}

h4 {
    color: #2980b9;
    margin-bottom: 5px;
}

h2 {
    color: #34495e;
    border-left: 4px solid #3498db;
    padding-left: 15px;
    margin-top: 30px;
}

strong {
    color: #2c3e50;
}

a {
    color: #3498db;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 15px 0;
}

th, td {
    text-align: left;
    padding: 8px;
    border-bottom: 1px solid #ddd;
}

th {
    background-color: #f8f9fa;
    font-weight: bold;
}

ul {
    padding-left: 20px;
}

li {
    margin-bottom: 5px;
}

.profile-header {
    text-align: center;
    margin-bottom: 30px;
}

blockquote {
    border-left: 4px solid #f39c12;
    background-color: #fef9e7;
    margin: 15px 0;
    padding: 10px 15px;
    font-style: italic;
}

hr {
    border: none;
    height: 2px;
    background: linear-gradient(to right, #3498db, #transparent);
    margin: 25px 0;
}

code {
    background-color: #f4f4f4;
    padding: 2px 5px;
    border-radius: 3px;
    font-family: 'Courier New', monospace;
}
"""

# HTML completo
full_html = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CV - Fernando Olvera Rendón</title>
</head>
<body>
    {html_content}
</body>
</html>
"""

# Generar PDF
try:
    # Crear directorio exports si no existe
    Path('exports').mkdir(exist_ok=True)
    
    # Generar PDF
    html_doc = HTML(string=full_html)
    css_doc = CSS(string=css_content)
    
    pdf_path = 'exports/cv_fernando_olvera_updated.pdf'
    html_doc.write_pdf(pdf_path, stylesheets=[css_doc])
    
    print(f"✅ CV actualizado generado: {pdf_path}")
    print(f"🌐 Portfolio link incluido: https://fernando-olvera-portfolio.onrender.com")
    print("📄 El PDF ahora incluye el link al portfolio web")
    
except Exception as e:
    print(f"❌ Error generando PDF: {e}")