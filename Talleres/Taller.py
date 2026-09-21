class EjercicioUno:
    def sumaNumeros(self, numeroUno = 3, numeroDos = 6):
        resultado = numeroUno + numeroDos
        print(f"La suma es: {resultado}")

class EjercicioDos:
    def suma(self, num1, num2):
        resultado = num1 + num2
        print(f"el resultado de la suma es: {resultado}")

class EjercicioTres:
    def suma(self, num1, num2):
        resultado = num1 + num2
        print(f"el resultado de la suma es: {resultado}")

    def resta(self, num1, num2):
        resultado = num1 - num2
        print(f"el resultado de la resta es: {resultado}")

    def multiplicacion(self, num1, num2):
        resultado = num1 * num2
        print(f"el resultado de la multiplicacion es: {resultado}")

    def division(self, num1, num2):
        resultado = num1 / num2
        print(f"el resultado de la division es: {resultado}")

class EjercicioCuatro:
    def calificacionFinal(self):
        participacion = float(input("Ingresa nota de participacion: "))
        pParcial = float(input("Ingresa nota del Primer Parcial: "))
        sParcial = float(input("Ingresa nota del Segundo Parcial: "))
        fParcial = float(input("Ingresa nota del Parcial Final: "))
        notaFinal = ((participacion * 0.10) + (pParcial * 0.25) + (sParcial * 0.25) + (fParcial * 0.40))
        print(f"Calificacion final es: {notaFinal}")


operaciones = EjercicioTres()

def programa():
    while True:
        print("Bienvenido al programa de los papus")
        print("Opciones")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        try:
            opcion = int(input("Ingresa una opcion del menu: "))

            match opcion:
                case 1:
                    try:
                        numeroUno = int(input("Ingresa un numero: "))
                        numeroDos = int(input("Ingresa otro numero: "))
                        operaciones.suma(numeroUno, numeroDos)
                    except ValueError:
                        print("Error: Por favor Ingresa un numero valido.")
                case 2:
                    try:
                        numeroUno = int(input("Ingresa un numero: "))
                        numeroDos = int(input("Ingresa otro numero: "))
                        operaciones.resta(numeroUno, numeroDos)
                    except ValueError:
                        print("Error: Por favor Ingresa un numero valido.")
                case 3:
                    try:
                        numeroUno = int(input("Ingresa un numero: "))
                        numeroDos = int(input("Ingresa otro numero: "))
                        operaciones.multiplicacion(numeroUno, numeroDos)
                    except ValueError:
                        print("Error: Por favor Ingresa un numero valido.")
                case 4:
                    try:
                        numeroUno = int(input("Ingresa un numero: "))
                        numeroDos = int(input("Ingresa otro numero: "))
                        operaciones.division(numeroUno, numeroDos)
                    except ValueError:
                        print("Error: Por favor Ingresa un numero valido.")

                case 5:
                    print("Has Salido del programa.")
                    break

                case _:
                    print("Esta opcion no existe.")

        except ValueError:
            print("Error: Por favor Ingresa una opcion del menu")

programa()