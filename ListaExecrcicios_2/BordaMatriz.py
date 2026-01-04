# Dada uma matriz 5x5, crie um novo array 1D contendo todos os elementos da borda da matriz, em sentido 
# horário, começando pelo canto superior esquerdo.


import numpy as np

matriz = np.arange(25).reshape(5, 5)

topo = matriz[0, :]                 # linha superior
direita = matriz[1:-1, -1]          # coluna direita
baixo = matriz[-1, ::-1]            # linha inferior (invertida)
esquerda = matriz[-2:0:-1, 0]       # coluna esquerda (invertida)

borda = np.concatenate([topo, direita, baixo, esquerda])

print("Matriz:")
print(matriz)

print("\nElementos da borda (sentido horário):")
print(borda)
