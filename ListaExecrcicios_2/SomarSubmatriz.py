# Dada uma matriz (preenchida com zeros) adicione o valor 5 apenas ao bloco central 2x2.

import numpy as np

matriz = np.zeros((4, 4), dtype = int)
print (f"\nMatriz original:\n{matriz}\n")

matriz [1:3,1:3] += 5
print (f"Adicionando 5 ao bloco central:\n{matriz}\n")