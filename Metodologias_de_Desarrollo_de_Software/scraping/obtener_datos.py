# Importamos las bibliotecas necesarias
from bs4 import BeautifulSoup
import csv
import os

# Especificamos la carpeta que contiene los archivos HTML
folder_path = './Semestre_IV/'

# Recorremos todos los archivos en la carpeta
for filename in os.listdir(folder_path):
    # Solo procesamos los archivos HTML
    if filename.endswith('.html'):
        # Abrimos el archivo HTML
        with open(os.path.join(folder_path, filename), 'r', encoding='ISO-8859-1') as f:
            # Leemos el contenido del archivo
            contents = f.read()

        # Creamos un objeto Beautiful Soup con el contenido del archivo
        soup = BeautifulSoup(contents, 'html.parser')

        # Buscamos todas las filas en el código HTML de la página
        rows = soup.find_all('tr')

        # Abrimos el archivo CSV en modo escritura
        with open('alumnos1.csv', 'a', newline='') as csvfile:
            # Creamos el objeto writer
            writer = csv.writer(csvfile)

            # Iteramos sobre las filas
            for row in rows:
                # Buscamos todas las celdas en la fila
                cells = row.find_all('td')

                # Si la fila tiene al menos tres celdas, asumimos que es una fila de alumno
                if len(cells) >= 3:
                    # Extraemos el código y el nombre del alumno
                    codigo = cells[1].get_text()
                    nombre = cells[2].get_text()

                    # Si el nombre es "Nombres", nos saltamos esta fila
                    if nombre == "Nombres":
                        continue

                    # Escribimos el código y el nombre del alumno en el archivo CSV
                    writer.writerow([codigo, nombre])

