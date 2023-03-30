"""Recorre el listado del ejemplo y realiza las siguientes operaciones:

[18, 50, 210, 80, 145, 333, 70, 30]

Imprimir el número en caso de que sea múltiplo de 10 y menor que 200
Parar el programa si llega a un número mayor que 300
Organizar la lista mediante el método de ordenamiento merge sort
Dada la lista anterior y un valor 145 devolver el índice de 145 en la lista si 145 está en la lista, y −1 si 145 no está en la lista
"""

class OpreacionesLista: 
    def __init__(self, lista):
        self.lista = lista

    def multiplo(self):
        for i in self.lista:
            if i % 10 == 0 and i < 200:
                print(i)

    def ordenar(self):
        self.lista.sort()
        print(self.lista)

    def buscar(self, valor):
        if valor in self.lista:
            print(self.lista.index(valor))
        else:
            print(-1)

    def parar(self):
        for i in self.lista:
            if i > 300:
                break
            else:
                print(i)

lista = [18, 50, 210, 80, 145, 333, 70, 30]
op = OpreacionesLista(lista)
op.multiplo()
op.parar()
op.ordenar()
op.buscar(145)