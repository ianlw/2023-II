# Obtención de datos de alumnos

## Cursos de cada Semestre
Se ingresó y descargó cada página de alumnos por curso de cada uno de los cursos de los 4 semestres del presente ciclo académico 2023-II. Teniendo una totalidad de 34 cursos, dentro de los cuales se contemplan aquellos que tienen diferentes horarios, es decir, diferentes grupos de alumnos para un mismo curso. 

## Alumnos de cada curso
Se obtuvieron los resultados de la obtención de datos a través de código en python. sin embargo estos datos necesitan ser limpiados de caracteres innecesarios para nuestros fines, además de eliminar las inevitables repeticiones de alumnos al trabajar con cursos en los cuales la mayoría de alumnos son los mismos. 
```bash
python3 ./obtener_datos.py
```
## Limpieza del archivo csv 
Analizando el archivo csv de datos de los alumnos se observa que aquellas lineas que inician con una letra son las cuales no son necesarias para nuestros fines, es decir el archivo csv solo tendrá lineas que inicien con el código del alumno y este código está siempre comformado por números. 
```bash
# Eliminar cada linea del archivo de texto que comienze con una letra
sed -i '/^[a-zA-Z]/d' alumnos.csv
```
Aproximadamente cada alumnos se repite unas 6 veces, esto devido a que están inscritos en los 6 cursos correspondientes a cada semestre, por ello tenemos que eliminar estas repeticiones para no generar errores en el futuro. Usaremos el código escrito en python respectivo.
```bash
python3 ./eliminar_repeticiones.py
```
## Modificar los nombres 
Separar los Nombres, Apellidos Paternos y Maternos para su correcto uso. 
```bash
sed -i 's/-/,/g' ./alumnos.csv 
```

Despues de todos este trabajo tenemos como resultado los códigos y nombres completos de los alumnos listos para ser usados. 

