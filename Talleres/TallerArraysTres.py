class Estudiante:
    def __init__(self, nombre, edad, nota_final):
        self.nombre = nombre
        self.edad = edad
        self.nota_final = nota_final

    def info_estudiante(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Nota final: {self.nota_final}")

estudiantePro = Estudiante("Daniel", 21, 4.4)

arrayEstudiantes = []
arrayEstudiantes.append(estudiantePro)

def registrar_estudiante(nombre, edad, nota_final):
    registroNuevo = Estudiante(nombre, edad, nota_final)
    arrayEstudiantes.append(registroNuevo)
    print("Registro con exito")

def menu():
    while True:
        print("")
        print("Menu Escuela")
        print("1. Registrar Estudiante")
        print("2. Listado Estudiantes")
        print("3. Salir")
        print("")

        try:
            opcion = int(input("Ingresa una opcion del menu: "))

            match opcion:
                case 1:
                    print("Registra un nuevo estudiante")
                    nombre = input("Ingresa el nombre del estudiante: ")
                    edad = int(input("Ingresa la edad del estudiante: "))
                    nota_final = float(input("Ingresa la nota final: "))
                    registrar_estudiante(nombre, edad, nota_final)

                case 2:
                    for i in range(len(arrayEstudiantes)):
                        estudiante = arrayEstudiantes[i]
                        estudiante.info_estudiante()
                    print("")
                case 3:
                    print("Has salido del programa")
                    break


        except ValueError:
            print("Opcion no valida")

menu()