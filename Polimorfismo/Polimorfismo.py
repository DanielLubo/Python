class Persona():
    def __init__(self, firts_name, last_name, id):
        self.firts_name = firts_name
        self.last_name = last_name
        self.id = id

    def presentar_persona(self):
        print(f"Nombre: {self.firts_name}")
        print(f"Apellido: {self.last_name}")
        print(f"Cedula: {self.id}")

usuario = Persona("Daniel", "Lubo", 1059235136)
usuario.presentar_persona()