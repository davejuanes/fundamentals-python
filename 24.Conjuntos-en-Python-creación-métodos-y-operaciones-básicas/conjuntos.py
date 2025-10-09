# Conjunto (set): Colección no ordenada de elementos únicos (no se puede acceder por indice)

frutas = ["Manzana", "Naranja", "Mandarina", "Naranja"]
print(frutas)
print(type(frutas))
print(len(frutas))

print("Manzana" in frutas)
print("Pera" not in frutas)

# Agregar
# Add
frutas = {"Manzana", "Naranja", "Mandarina", "Naranja"}
frutas.add("Pera")
print(frutas)

# Update
frutasTropicales = {"Piña", "Mango"} # Agregar lstas, tuplas, conjuntos
frutas.update(frutasTropicales)

conjuntos = {"Python", 156, True}
print(conjuntos)
print(type(conjuntos))

for item in conjuntos:
    print(item)

# Eliminarlos
frutas.remove("Mango")
print(frutas)

# Discard
frutas.discard("Pera")
print(frutas)
# Pop
frutas.pop()
print(frutas)
# Clear
frutas.clear()
print(frutas)

print("-----------------")

a = {"a", "b", "c"}
b = {"c", "d", "e"}

c = a.union(b)
print(c)

i = a.intersection(b)
print(i)

d = a.difference(b)
print(d)