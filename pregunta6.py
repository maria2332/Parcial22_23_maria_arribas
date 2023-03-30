"""
Realiza el  código para calcular el determinante de una matriz cuadrada de [5 x 5], regla de Sarrus de forma recursiva y de forma iterativa
"""

def sarrus(matriz, n):
    if n == 1:
        return matriz[0][0]
    else:
        det = 0
        for i in range(n):
            det += matriz[0][i] * sarrus(matriz[1:], n-1)
        return det
    
def sarrus_iterativo(matriz, n):
    det = 0
    for i in range(n):
        det += matriz[0][i] * sarrus(matriz[1:], n-1)
    return det

matriz = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
print(sarrus(matriz, 5))
print(sarrus_iterativo(matriz, 5))

