import csv

# Abrimos el archivo CSV en modo lectura
with open('alumnos.csv', 'r') as csvfile:
    # Leemos el archivo CSV en un diccionario
    reader = csv.reader(csvfile)
    data = {rows[0]: rows[1] for rows in reader}

# Abrimos el archivo CSV en modo escritura
with open('alumnos.csv', 'w', newline='') as csvfile:
    # Creamos el objeto writer
    writer = csv.writer(csvfile)
    
    # Escribimos los datos en el archivo CSV
    for codigo, nombre in data.items():
        writer.writerow([codigo, nombre])

