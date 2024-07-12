# AutoCV: De LinkedIn a PDF con Modelos LLM

**AutoCV** es un proyecto que automatiza la generación de un Curriculum Vitae (CV) profesional. Utilizando datos extraídos de LinkedIn, los formatea en Markdown mediante un modelo de lenguaje de gran escala (LLM), y finalmente convierte ese Markdown en un archivo PDF estilizado.

## Requisitos

- Python 3.x
- `wkhtmltopdf` instalado y accesible en `C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe`
- Librerías de Python:
  - `pdfkit`
  - `requests`
  - `markdown2`

## Instalación

1. **Clonar el repositorio**:

   ```bash
   git clone https://github.com/vlasvlasvlas/curriculum-cv.git
   cd curriculum-cv
   ```

2. **Crear y activar un entorno virtual**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar las dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Instalar `wkhtmltopdf`**:

   Descarga e instala `wkhtmltopdf` desde [wkhtmltopdf releases](https://wkhtmltopdf.org/downloads.html).

## Uso

1. **Ejecutar el script de conversión**:

   ```bash
   python create-cv.py
   ```

   Esto descargará el archivo Markdown desde GitHub, lo convertirá a HTML y luego generará un archivo PDF con el nombre `Vladimiro_Bellini_CV_yyyy-mm-dd.pdf`, donde `yyyy-mm-dd` es la fecha actual.

## Estructura del Proyecto

```plaintext
curriculum-cv/
├── venv/
├── .gitattributes
├── .gitignore
├── create-cv.py
├── curriculum-cv.md
├── README.md
├── requirements.txt
└── Vladimiro_Bellini_CV_yyyy-mm-dd.pdf
```

- `venv/`: Entorno virtual para las dependencias de Python.
- `.gitattributes` y `.gitignore`: Archivos de configuración de Git.
- `create-cv.py`: Script de Python para convertir el archivo Markdown a PDF.
- `curriculum-cv.md`: Archivo Markdown con el contenido del CV.
- `README.md`: Este archivo, proporcionando detalles del proyecto.
- `requirements.txt`: Archivo de requisitos que lista las dependencias de Python.
- `Vladimiro_Bellini_CV_yyyy-mm-dd.pdf`: El archivo PDF generado.

## TODO

### Generación Automática del Curriculum

- **Extracción de Datos desde LinkedIn**:
  - Implementar un script que realice scraping de LinkedIn (con el consentimiento del usuario) para extraer la información relevante del perfil del usuario.

- **Conversión con Modelos LLM**:
  - Utilizar un modelo de lenguaje de gran escala (LLM) para procesar y formatear la información extraída en un archivo Markdown simplificado y atractivo.

- **Automatización del Flujo Completo**:
  - Desarrollar un flujo automatizado que tome los datos extraídos de LinkedIn, los procese con el LLM y genere el archivo Markdown.
  - Convertir automáticamente el archivo Markdown a PDF utilizando el script actual, estilizando el PDF para que tenga una apariencia profesional.

## Contribuir

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva funcionalidad'`).
4. Envía los cambios a tu fork (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo [LICENSE](LICENSE).
