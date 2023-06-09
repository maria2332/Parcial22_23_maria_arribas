"""
Creación (0,5 puntos)
Copia el ejercicio anterior y realicemos una modificación:

Junto al método init y calificación, vamos a crear otro método especial de Python, el método str. Al igual que init, debe ir encerrado entre dobles guiones bajos, y debe tener el siguiente formato:

 

def __str__(self): return "Lo que quiero mostrar"

 

Este método nos sirve para imprimir por pantalla la información de un objeto, si tenemos un objeto alumno1 creado y realizamos print(alumno1), Python ejecutará el contenido del método str (el método str lo que tiene que hacer es maquetar la información que desea en un string).

 

Experimentación (0,5 puntos)
Implementa el método str y haz que muestre el nombre y la nota del alumno
Crea algun objeto de la clase Alumno
Realiza print de esos objetos para visualizar por pantalla la información del str
"""

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("El alumno se ha creado con éxito")

    def __str__(self):
        return f"El alumno se llama {self.nombre} y tiene una nota de {self.nota}"
    
    def calificacion(self, nota, nombre):
        if self.nota >= 5:
            print(f"{nombre} ha aprobado con un {nota}")
        else:
            print(f"{nombre} ha suspendido con un {nota}")

if __name__ == "__main__":
    alumno1 = Alumno("Maria", 10)
    alumno2 = Alumno("Pedro", 3)
    alumno1.calificacion(alumno1.nota, alumno1.nombre)
    alumno2.calificacion(alumno2.nota, alumno2.nombre)
    print(alumno1)
    print(alumno2)