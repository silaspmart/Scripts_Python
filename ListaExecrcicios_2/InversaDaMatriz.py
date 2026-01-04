# Calcule a matriz inversa da matriz A. Depois, verifique seu trabalho calculando o produto de A 
# pela sua inversa (o resultado deve ser a matriz identidade). 
# 
# A matriz inversa de uma matriz quadrada A é outra matriz, chamada A⁻¹, que quando multiplicada 
# por A resulta na matriz identidade (uma matriz que tem 1 na diagonal principal e 0 nos outros 
# elementos). Em outras palavras, A × A⁻¹ = I. A inversa só existe para matrizes quadradas que não sejam 
# singulares, ou seja, que tenham determinante diferente de zero. Ela é usada para resolver sistemas 
# lineares, desfazer transformações e em várias aplicações de álgebra linear.

import numpy as np

A = np.array([[4, 7], [2, 6]])
A_inv = np.linalg.inv(A)

print(f"Matriz original:\n {A}\n")
print(f"Matriz inversa de A:\n{A_inv}\n")

identidade = A @ A_inv

# Verificação: A × A⁻¹ = I

print(f"A × A⁻¹:\n {identidade}\n")

det = np.linalg.det(A)
print(det.round(2))