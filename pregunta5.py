"""
La alianza rebelde necesita comunicarse de manera segura pero el imperio galáctico interviene todas la comunicaciones, por lo que la princesa Leia nos encarga el desarrollo de un algoritmo de encriptación para las comunicaciones rebeldes, que contemple los siguientes requerimientos:

 cada carácter deberá ser encriptado a ocho caracteres;
 se deberá generar dos tablas hash para encriptar y desencriptar, para los caracteres desde el “ ” hasta el “}” –es decir desde el 32 al 125 de la tabla ASCII.
 """

class Encriptar:
    def __init__(self, mensaje):
        self.mensaje = mensaje
        self.tabla_encriptar = {}
        self.tabla_desencriptar = {}
        self.mensaje_encriptado = ""
        self.mensaje_desencriptado = ""
        self.generar_tablas()
        self.encriptar()
        self.desencriptar()

    def generar_tablas(self):
        for i in range(32, 126):
            self.tabla_encriptar[chr(i)] = self.generar_caracter_encriptado(chr(i))
            self.tabla_desencriptar[self.tabla_encriptar[chr(i)]] = chr(i)

    def generar_caracter_encriptado(self, caracter):
        caracter_encriptado = ""
        for i in range(8):
            caracter_encriptado += chr(ord(caracter) + i)
        return caracter_encriptado

    def encriptar(self):
        for caracter in self.mensaje:
            self.mensaje_encriptado += self.tabla_encriptar[caracter]

    def desencriptar(self):
        for i in range(0, len(self.mensaje_encriptado), 8):
            self.mensaje_desencriptado += self.tabla_desencriptar[self.mensaje_encriptado[i:i+8]]

    def __str__(self):
        return f"Mensaje original: {self.mensaje} \nMensaje encriptado: {self.mensaje_encriptado} \nMensaje desencriptado: {self.mensaje_desencriptado}" 
    
if __name__ == "__main__":
    mensaje = "Hola mundo"
    encriptar = Encriptar(mensaje)
    print(encriptar) 