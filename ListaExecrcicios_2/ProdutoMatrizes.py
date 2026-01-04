# Dadas as duas matrizes A e B, calcule o produto matricial entre A e B.

import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])     
B = np.array([[7, 8], [9, 10], [11, 12]]) 

produto_matricial = A@B
print (f"Primeira matriz:\n {A}")
print (f"\nSegunda matriz:\n {B}")
print (f"\nProduto matricial:\n {produto_matricial}\n")