import requests
import markdown2
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import os
from bs4 import BeautifulSoup

# URL del archivo Markdown en GitHub
url = "https://raw.githubusercontent.com/vlasvlasvlas/curriculum-cv/main/curriculum-cv.md"
response = requests.get(url)

# Nombre del archivo temporal para almacenar el Markdown
markdown_file = "curriculum-cv.md"
with open(markdown_file, 'w', encoding='utf-8') as file:
    file.write(response.text)

# Leer contenido del archivo Markdown
with open(markdown_file, 'r', encoding='utf-8') as file:
    markdown_content = file.read()

# Convertir Markdown a HTML
html_content = markdown2.markdown(markdown_content)

# Obtener la fecha actual en formato yyyy-mm-dd
current_date = datetime.now().strftime('%Y-%m-%d')

# Nombre del archivo PDF con la fecha
pdf_filename = f'Vladimiro_Bellini_CV_{current_date}.pdf'

# Crear el PDF usando reportlab
def create_pdf(content, filename):
    pdf_canvas = canvas.Canvas(filename, pagesize=letter)
    pdf_canvas.setTitle("Curriculum Vitae")
    width, height = letter

    y_position = height - 40
    x_position = 40
    max_width = width - 2 * x_position

    # Convertir contenido HTML a texto plano
    soup = BeautifulSoup(content, 'html.parser')
    for element in soup.descendants:
        if element.name in ['h1', 'h2', 'h3']:
            pdf_canvas.setFont("Helvetica-Bold", 12)
            text = element.get_text()
        elif element.name in ['p', 'li']:
            pdf_canvas.setFont("Helvetica", 10)
            text = element.get_text()
        else:
            continue

        for line in text.split('\n'):
            pdf_canvas.drawString(x_position, y_position, line)
            y_position -= 12
            if y_position < 40:
                pdf_canvas.showPage()
                y_position = height - 40

    pdf_canvas.save()

create_pdf(html_content, pdf_filename)

# Eliminar el archivo temporal Markdown
os.remove(markdown_file)

print(f"PDF creado exitosamente: {pdf_filename}")
