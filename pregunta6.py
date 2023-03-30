"""
Realiza el  código para calcular el determinante de una matriz cuadrada de [5 x 5], regla de Sarrus de forma recursiva y de forma iterativa
"""

#Sarrus solo se puede usar en matrices de 3x3, por lo tanto, para matrices de 5x5 necesitaremos descomponer la matriz en submatrices de 3x3 y aplicar la regla de Sarrus a cada una de ellas.

def determinante_sarrus_recursivo(matriz):
    if len(matriz) != 5 or len(matriz[0]) != 5:
        raise ValueError("La matriz debe ser cuadrada de 5x5")

    if len(matriz) == 1:
        return matriz[0][0]
    
    # Calcular el determinante utilizando la regla de Sarrus
    det = 0
    for j in range(5):
        cofactor = (-1) ** (2+j) * matriz[2][j] * (matriz[3][(j+1)%5] * matriz[4][(j+2)%5] - matriz[3][(j+2)%5] * matriz[4][(j+1)%5])
        det += cofactor * matriz[0][j]

    # Llamar recursivamente a la función para calcular el determinante de la matriz de menor tamaño
    submatriz = [fila[1:] for fila in matriz[1:]]
    det += determinante_sarrus_recursivo(submatriz) * matriz[0][0]

    return det

def determinante_sarrus_iterativo(matriz):
    if len(matriz) != 5 or len(matriz[0]) != 5:
        raise ValueError("La matriz debe ser cuadrada de 5x5")

    # Crear una matriz auxiliar para aplicar la regla de Sarrus
    aux = matriz + matriz[:2]

    # Sumar los productos diagonales de izquierda a derecha
    det = 0
    for j in range(5):
        producto = 1
        for i in range(5):
            producto *= aux[i+j][i]
        det += producto

    # Restar los productos diagonales de derecha a izquierda
    for j in range(5):
        producto = 1
        for i in range(5):
            producto *= aux[i+j][-i-1]
        det -= producto

    return det

matriz = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]

det = determinante_sarrus_recursivo(matriz)
print("El determinante calculado de forma recursiva es:", det)

det = determinante_sarrus_iterativo(matriz)
print("El determinante calculado de forma iterativa es:", det)