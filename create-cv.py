import requests
import markdown2
import pdfkit
from datetime import datetime
import os

# Ruta al ejecutable wkhtmltopdf
path_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"

# Verificar si wkhtmltopdf está instalado
if not os.path.isfile(path_wkhtmltopdf):
    print("wkhtmltopdf no está instalado en la ruta especificada.")
    exit(1)

# Configuración de pdfkit
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

# URL del archivo Markdown en GitHub
url = "https://raw.githubusercontent.com/vlasvlasvlas/curriculum-cv/main/curriculum-cv.md"
response = requests.get(url)

# Leer contenido del archivo Markdown
markdown_content = response.text

# Convertir Markdown a HTML
html_content = markdown2.markdown(markdown_content, extras=["fenced-code-blocks"])

# Agregar estilos CSS para definir la tipografía
html_content_with_css = f"""
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<style>
    body {{
        font-family: Arial, Helvetica, sans-serif;
        line-height: 1.6;
    }}
    h1, h2, h3, h4, h5, h6 {{
        font-family: Arial, Helvetica, sans-serif;
    }}
    p {{
        font-family: Arial, Helvetica, sans-serif;
    }}
    ul {{
        font-family: Arial, Helvetica, sans-serif;
    }}
</style>
</head>
<body>
{html_content}
</body>
</html>
"""

# Obtener la fecha actual en formato yyyy-mm-dd
current_date = datetime.now().strftime('%Y-%m-%d')

# Nombre del archivo PDF con la fecha
pdf_filename = f'Vladimiro_Bellini_CV_{current_date}.pdf'

# Opciones para pdfkit para manejar correctamente el encoding
options = {
    'encoding': 'UTF-8',
}

# Convertir HTML a PDF usando pdfkit
pdfkit.from_string(html_content_with_css, pdf_filename, configuration=config, options=options)

print(f"PDF creado exitosamente: {pdf_filename}")
