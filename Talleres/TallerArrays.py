arrayMascotas = []

class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad

    def info_mascota(self):
        print(f"Nombre: {self.nombre}")
        print(f"Especie: {self.especie}")
        print(f"Edad: {self.edad}")


mascotaUno = Mascota("Hachiko", "Shibainu", 2)
arrayMascotas.append(mascotaUno)

def menu():
    while True:
        print("")
        print("Menu Veterinaria Pro")
        print("1. Adicionar Mascota")
        print("2. Mostrar Lista de Mascotas")
        print("3. Salir")
        print("")

        try:
            opcion = int(input("Ingresa una opcion del menu: "))
            match opcion:
                case 1:
                    try:
                        print("Registra nueva Mascota")
                        nombre = input("Ingresa el nombre de la mascota: ")
                        especie = input("Ingresa la especie de la mascota: ")
                        edad = int(input("Ingresa la edad de la mascota:"))
                        nuevoRegistro = Mascota(nombre, especie, edad)
                        arrayMascotas.append(nuevoRegistro)
                    except ValueError:
                        9

                case 2:
                    print("")
                    print("Mascotas registradas")
                    for i in range(len(arrayMascotas)):
                        mascota = arrayMascotas[i]
                        mascota.info_mascota()
                    print("")
                case 3:
                    print("Has salido del programa")
                    break
        except ValueError:
            print("Opcion no valida")

menu()