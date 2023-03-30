"""Recorre el listado del ejemplo y realiza las siguientes operaciones:

[18, 50, 210, 80, 145, 333, 70, 30]

Imprimir el número en caso de que sea múltiplo de 10 y menor que 200
Parar el programa si llega a un número mayor que 300
Organizar la lista mediante el método de ordenamiento merge sort
Dada la lista anterior y un valor 145 devolver el índice de 145 en la lista si 145 está en la lista, y −1 si 145 no está en la lista
"""

class OperacionesLista:
    def __init__(self, numeros):
        self.numeros = numeros

    def imprimir_multiplos_10_menores_200(self):
        for num in self.numeros:
            if num % 10 == 0 and num < 200:
                print(num)

            # Si encontramos un número mayor que 300, detenemos el programa
            if num > 300:
                break

    def merge_sort(self):
        def mergesort(lista):
            """ Método de ordenamiento mergesort"""
            if len(lista) <= 1:
                return lista
            else:
                medio = len(lista) // 2  # se parte la lista en dos
                izquierda = []
                for i in range(0, medio):
                    izquierda.append(lista[i])  # se copia la primera mitad
                derecha = []
                for i in range(medio, len(lista)):
                    derecha.append(lista[i])  # se copia la segunda mitad
                izquierda = mergesort(izquierda)  # llamada recursiva
                derecha = mergesort(derecha)  # llamada recursiva
                resultado = merge(izquierda, derecha)
                return resultado

        def merge(izquierda, derecha):
            """ Función auxiliar para el método mergesort"""
            lista_mezclada = []
            while len(izquierda) > 0 and len(derecha) > 0:
                if izquierda[0] < derecha[0]:
                    lista_mezclada.append(izquierda.pop(0))
                else:
                    lista_mezclada.append(derecha.pop(0))
            if len(izquierda) > 0:
                lista_mezclada += izquierda
            if len(derecha) > 0:
                lista_mezclada += derecha
            return lista_mezclada

        return mergesort(self.numeros)

    def buscar_indice(self, valor):
        if valor in self.numeros:
            return self.numeros.index(valor)
        else:
            return -1

if __name__ == "__main__":
    lista = [18, 50, 210, 80, 145, 333, 70, 30]
    operaciones = OperacionesLista(lista)
    operaciones.imprimir_multiplos_10_menores_200()
    print(operaciones.merge_sort())
    print(operaciones.buscar_indice(145))
    print(operaciones.buscar_indice(1000))
   