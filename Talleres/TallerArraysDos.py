class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def info_producto(self):
        print(f"Codigo del producto: {self.codigo}")
        print(f"Nombre del producto: {self.nombre}")
        print(f"Precio del producto: {self.precio}")

# Producto Registrado
nuevoProducto = Producto(1223, "Ryzen 5 9600x", 560000)

arrayProductos = []
arrayProductos.append(nuevoProducto)

def agregar_producto(codigo, nombre, precio):
    nuevoProductoRegistrado = Producto(codigo, nombre, precio)
    arrayProductos.append(nuevoProductoRegistrado)
    print("Producto Registrado con Exito")


def menu():
    while True:
        print("")
        print("Menu de tienda Productos")
        print("1. Agregar Producto")
        print("2. Mostrar Lista de Productos")
        print("3. Salir")

        try:
            opcion = int(input("Ingresa una opcion del menu:"))

            match opcion:
                case 1:
                    print("Registra un nuevo producto")
                    codigo = int(input("Ingresa codigo del Producto: "))
                    nombre = input("Ingresa nombre del Producto: ")
                    precio = int(input("Ingresa el precio del Producto: "))
                    agregar_producto(codigo, nombre, precio)

                case 2:
                    print("Productos Registrados")
                    for i in range(len(arrayProductos)):
                        producto = arrayProductos[i]
                        producto.info_producto()

                    print("")

                case 3:
                    print("Has salido del programa")
                    break
        except ValueError:
            print("Ingresa un numero")


menu()


