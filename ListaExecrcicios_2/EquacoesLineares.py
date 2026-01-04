# Resolva o seguinte sistema de equações lineares:
# 2x + y = 8
# x + 3y = 7
# Represente o sistema na forma matricial Ax = b e encontre o vetor x (que contém os valores de x e y).

import numpy as np

A = np.array([[2, 1], [1, 3]])
b = np.array([8, 7])

solucao = np.linalg.solve(A, b)

x, y = solucao

print(f"x = {x}")
print(f"y = {y}")
