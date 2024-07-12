from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from markdown import markdown
from datetime import datetime
import os

def create_pdf(content, filename):
    pdf_canvas = canvas.Canvas(filename, pagesize=letter)
    pdf_canvas.setTitle("Curriculum Vitae")
    width, height = letter

    # Divide el contenido en líneas
    lines = content.split('\n')
    text_object = pdf_canvas.beginText(40, height - 40)
    text_object.setFont("Helvetica", 12)

    for line in lines:
        # Aquí puedes agregar lógica para procesar el contenido, por ejemplo,
        # agregar saltos de línea si la línea es muy larga.
        text_object.textLine(line)

    pdf_canvas.drawText(text_object)
    pdf_canvas.save()

# Leer contenido del archivo Markdown
with open('curriculum-cv.md', 'r', encoding='utf-8') as file:
    markdown_content = file.read()

# Convertir Markdown a texto plano
plain_text = markdown(markdown_content, output_format='html')

# Obtener la fecha actual en formato yyyy-mm-dd
current_date = datetime.now().strftime('%Y-%m-%d')

# Nombre del archivo PDF con la fecha
pdf_filename = f'Vladimiro_Bellini_CV_{current_date}.pdf'

# Crear el PDF
create_pdf(plain_text, pdf_filename)

print(f"PDF creado exitosamente: {pdf_filename}")
