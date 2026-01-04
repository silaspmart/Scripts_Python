# Dado uma matriz 4x4, crie um novo array contendo apenas os elementos da terceira coluna.

import numpy as np

matriz = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])

nova_matriz = matriz[:,2]
print(f"\nElementos da 3ª coluna:\n {nova_matriz} \n")
