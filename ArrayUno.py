notas = [0, 3.0, 4.2, 5]

print("Lista de notas:", notas)

# Agregar al final de la lista
notas.append(1)
print("Lista de notas nueva:", notas)

# Agrega un elemento en un indice especifico de la lista
notas.insert(2, 4.7)
print("Lista de notas con insert:", notas)

# Agregar valor a un indice de forma manual
notas[0] = 1.2
print("Lista de notas de forma manual:", notas)

# Eliminar un nota por valor
notas.remove(4.7)
print("Lista de notas despues de eliminar:", notas)

# Eliminar una nota por posicion
eliminada = notas.pop(3)
print("Lista de notas despues de eliminar:", notas)

# Recorrer la Lista con for in
print("Recorre el coso")
for i in range (len(notas)):
    print("Posicion ", i, "->", notas[i])

# Calcular la cantidad - Longitud del array
cantidad = len(notas)
print("La longitud es:", cantidad)

# Realizar la suma del coso
suma = 0
for nota in notas:
    suma += nota
    print(suma)

promedio = suma / len(notas)
print(f"El promedio es: {promedio}")

# Suma eficiente
print(f"La suma eficiente es: {sum(notas)}")
print(f"El promedio eficiente es: {sum(notas) / len(notas)}")



print("Nota mayor")
nota_mayor = 0
for i in range (len(notas)):
    if notas[i] > nota_mayor:
        nota_mayor = notas[i]

print(f"La nota mayor es: {nota_mayor}")