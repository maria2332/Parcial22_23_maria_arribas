"""
Realiza el  código para calcular el determinante de una matriz cuadrada de [5 x 5], regla de Sarrus de forma recursiva y de forma iterativa
"""

#Sarrus solo se puede usar en matrices de 3x3, por lo tanto, para matrices de 5x5 necesitaremos descomponer la matriz en submatrices de 3x3 y aplicar la regla de Sarrus a cada una de ellas.

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

    def __str__(self):
        return f"{self.dato}"
