# Dada uma matriz, crie uma nova matriz onde todos os números maiores que 8 sejam substituídos pelo 
# valor -1. Crie uma cópia da matriz antes de fazer a operação.

import numpy as np

dados = np.arange(16).reshape(4, 4)
print (f"Matriz inicial:\n {dados}\n")

nova_matriz = dados.copy()
nova_matriz[nova_matriz > 8] = -1

print("\nNova matriz:")
print(nova_matriz)