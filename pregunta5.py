"""
La alianza rebelde necesita comunicarse de manera segura pero el imperio galáctico interviene todas la comunicaciones, por lo que la princesa Leia nos encarga el desarrollo de un algoritmo de encriptación para las comunicaciones rebeldes, que contemple los siguientes requerimientos:

 cada carácter deberá ser encriptado a ocho caracteres;
 se deberá generar dos tablas hash para encriptar y desencriptar, para los caracteres desde el “ ” hasta el “}” –es decir desde el 32 al 125 de la tabla ASCII.
 """


class Encriptacion:
    def __init__(self, texto):
        self.texto = texto
        self.tabla_encriptar = {}
        self.tabla_desencriptar = {}
        self.encriptado = ""
        self.desencriptado = ""
        self.generar_tablas()

    def generar_tablas(self):
        for i in range(32, 126):
            self.tabla_encriptar[chr(i)] = chr(i + 8)
            self.tabla_desencriptar[chr(i + 8)] = chr(i)

    def encriptar(self):
        for i in self.texto:
            self.encriptado += self.tabla_encriptar[i]
        return self.encriptado

    def desencriptar(self):
        for i in self.encriptado:
            self.desencriptado += self.tabla_desencriptar[i]
        return self.desencriptado

    def __str__(self):
        return f"Texto encriptado: {self.encriptado} Texto desencriptado: {self.desencriptado}"
    
texto = "Hola mundo"
encriptacion = Encriptacion(texto)
print(encriptacion.encriptar())
print(encriptacion.desencriptar())
print(encriptacion)