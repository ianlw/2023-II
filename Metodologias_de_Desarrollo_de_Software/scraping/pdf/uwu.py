import re

# Tu texto
text = """
1. DR. LAURO ENCISO RODAS     PR-DE   ____________________   
2. MGT. JULIO CÉSAR CARBAJAL LUNA    PR-DE   ____________________   
3. MGT. NILA ZONIA ACURIO USCA    PR-DE   ________ ____________   
...
24. MGT. HARLEY VERA OLIVERA     AU-TC  ____________________   
"""

# Patrón para coincidir con los nombres de los docentes
pattern = r'\d+\.\s+DR\.|MGT\.|ING\.|LIC\.\s+([A-ZÁÉÍÓÚ\s]+)\s+PR-DE|PR-TC|AS-TC|AS-DE|AS-TP|AU-TC'

# Busca todas las coincidencias en el texto
matches = re.findall(pattern, text)

# Imprime los nombres de los docentes
for match in matches:
    print(match.strip())

