from PyPDF2 import PdfReader

# Crea un objeto de la clase PdfReader
reader = PdfReader('./docentes.pdf')

# Obtiene el número de páginas en el archivo PDF
print(len(reader.pages))

# Obtiene la primera página del archivo PDF
page = reader.pages[0]

# Extrae el texto de la página
text = page.extract_text()

# Imprime el texto extraído
print(text)

