class Vehiculo:
    def __init__(self, placa, marca, modelo):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo

    def info_vehiculo(self):
        print(f"Placa: {self.placa}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")

nuevoCarro = Vehiculo("SSH 453", "BMW", 2021)

arrayVehiculo = []
arrayVehiculo.append(nuevoCarro)

def registrar_vehiculo(placa, marca, modelo):
    registroNuevo = Vehiculo(placa, marca,  modelo)
    arrayVehiculo.append(registroNuevo)
    print("Registro con exito")

def menu():
    while True:
        print("")
        print("Menu Escuela")
        print("1. Registrar Vehiculo")
        print("2. Listado Vehiculo")
        print("3. Salir")
        print("")

        try:
            opcion = int(input("Ingresa una opcion del menu: "))

            match opcion:
                case 1:
                    print("Registra un nuevo estudiante")
                    placa = input("Ingresa la placa: ")
                    marca = input("Ingresa la marca del vehiculo: ")
                    modelo = int(input("Ingresa el modelo: "))
                    registrar_vehiculo(placa, marca, modelo)

                case 2:
                    for i in range(len(arrayVehiculo)):
                        vehiculo = arrayVehiculo[i]
                        vehiculo.info_vehiculo()
                    print("")
                case 3:
                    print("Has salido del programa")
                    break


        except ValueError:
            print("Opcion no valida")

menu()