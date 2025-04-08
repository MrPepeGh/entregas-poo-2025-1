from datetime import datetime

class Mascota:
    def __init__(self, nombre, edad, raza):
        self.nombre = nombre
        self.edad = edad
        self.raza = raza
        self.fecha_ingreso = datetime.now().astimezone().isoformat()
    def obtener_clase(self):
        return self.__class__.__name__
    def mostrar_info(self):
        clase = self.obtener_clase()
        return f"|{clase:<6}|{self.nombre:<9}|{self.edad} años |{self.raza:<13}|{self.fecha_ingreso} |"
    '''definimos las clases de las mascotas que se pueden adminit'''
class Perro(Mascota):
    pass
class Gato(Mascota):
    pass
class Ave(Mascota):
    pass
def ingresar_mascota(numero):
    while True:
        clase = input(f"> Mascota {numero}, que clase es (P)Perro, (G)Gato o (A)Ave?\n< ").strip().lower()
        if clase in ['p', 'g', 'a']:
            break
        print("Entrada inválida. Ingresa 'P' para perro, 'G' para gato o 'A' para ave.")
    '''Hacemos que se identifique qué clase de las 3 es la mascota'''
    tipo = {"p": "Perro", "g": "Gato", "a": "Ave"}[clase]
    nombre = input(f"> cual es el nombre del {tipo}?\n< ").strip()
    edad = int(input(f"> que edad tiene '{nombre}'?\n< "))
    raza = input(f"> de que raza es '{nombre}'?\n< ").strip()
    if clase == 'p':
        return Perro(nombre, edad, raza)
    elif clase == 'g':
        return Gato(nombre, edad, raza)
    else:
        return Ave(nombre, edad, raza)
def main():
    mascotas = []
    cantidad = int(input("> Cuantas mascotas va a ingresar?\n< "))
    for i in range(1, cantidad + 1):
        mascota = ingresar_mascota(i)
        mascotas.append(mascota)
    print("\n> Resumen:")
    print("> |Clase |Nombre   |Edad   |Raza         |Fecha de ingreso          |")
    for m in mascotas:
        print("> " + m.mostrar_info())
if __name__ == "__main__":
    main()
