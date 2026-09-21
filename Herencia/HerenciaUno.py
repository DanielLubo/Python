class Animal:
    def comer(self):
        print('Come muchas veces en el dia')

    def dormir(self):
        print("Duerme muchas horas")

class Perro(Animal):
    def hacer_sonido(self):
        print("Puedo ladrar")


print("Herencia en python")
print("Clase padre, animal")
animalUno = Animal()
animalUno.comer()
animalUno.dormir()

print("\nClase Hija, perro")
animalDos = Perro()
animalDos.comer()
animalDos.hacer_sonido()