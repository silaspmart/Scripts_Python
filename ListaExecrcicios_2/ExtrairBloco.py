# A partir da mesma matriz do exercício 1, extraia o bloco central 2x2, que contém 
# os números 6, 7, 10 e 11.

import numpy as np

matriz = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

bloco_central = matriz[1:3,1:3]
print(f"Matriz central 2x2: \n {bloco_central}\n")