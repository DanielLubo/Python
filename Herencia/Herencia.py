class Animal():
    def __init__(self, name, age, weight  ):
        self.name = name
        self.age = age
        self.weight = weight

    def ladrar(self, sonido):
        return f"El animal hace: {sonido}"

class Perro(Animal):
    def ladrar(self, sonido = "guau"):
        return f"El {self.name} hace: {sonido}"

hachiko = Perro("Hachiko", 12, 34)
print(hachiko.ladrar())