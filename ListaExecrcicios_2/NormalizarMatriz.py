# Normalize a matriz abaixo. A normalização (Z-score) é feita subtraindo a média de todos os 
# elementos de cada elemento e, em seguida, dividindo pelo desvio padrão.
# Fórmula: (X - media) / desvio_padrao.

import numpy as np

matriz = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print (f"Matriz original:\n{matriz}")

media = matriz.mean()
desvio = matriz.std()

print (f"\nMédia dos valores: {media}")
print (f"Desvio padrão da matriz: {desvio:.1f}")

normalizada = (matriz - media) / desvio
print (f"\nMatriz normalizada:\n {normalizada.round(1)}\n")