# Dada uma matriz 9x9 abaixo, crie um novo array que contenha apenas os valores das linhas 
# de índice par e as colunas de índice ímpar.

import numpy as np

matriz = np.arange(81).reshape(9, 9)
resultado = matriz[::2,1::2]
resultado_inv = matriz[1::2,::2]

print (f"\n Matriz Original:\n {matriz}\n")
print (f"\nMatriz com linhas pares e colunas ímpares:\n{resultado}")
print (f"\nMatriz com linhas ímpares e colunas pares:\n{resultado_inv}")