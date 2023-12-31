import numpy as np
import math
matriz_a = np.array([[math.cos(math.radians(45)), -math.sin(math.radians(45))], [math.sin(math.radians(45)), math.cos(math.radians(45))]])
matriz_b = np.array([[300], [300]])
resultado = np.dot(matriz_a, matriz_b)
