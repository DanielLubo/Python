class Libro:
    def __init__(self, codigo, titulo, autor):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor

    def info_libro(self):
        print(f"Codigo: {self.codigo}")
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")

nuevoLibro = Libro("SSH 453", "La rata con Thiner", "Si")

arrayLibro = []
arrayLibro.append(nuevoLibro)

def registrar_libro(codigo, titulo, autor):
    registroNuevo = Libro(codigo, titulo,  autor)
    arrayLibro.append(registroNuevo)
    print("Registro con exito")

def menu():
    while True:
        print("")
        print("Menu Libreria")
        print("1. Registrar Libro")
        print("2. Listado Libros")
        print("3. Salir")
        print("")

        try:
            opcion = int(input("Ingresa una opcion del menu: "))

            match opcion:
                case 1:
                    print("Registra un nuevo libro")
                    codigo = input("Ingresa el codigo: ")
                    titulo = input("Ingresa el titulo: ")
                    autor = int(input("Ingresa el autor: "))
                    registrar_libro(codigo, titulo, autor)

                case 2:
                    for i in range(len(arrayLibro)):
                        libro = arrayLibro[i]
                        libro.info_libro()
                    print("")
                case 3:
                    print("Has salido del programa")
                    break

        except ValueError:
            print("Opcion no valida")

menu()