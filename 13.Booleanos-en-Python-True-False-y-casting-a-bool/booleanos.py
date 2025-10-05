from re import X


v = True
f = False

print(v)
print(f)

print(5 > 3) # Verdadero
print(3 > 5) # False

print(type(v))

print(bool("Hola mundo"))
print(bool(""))

# True

print(bool("abc"))
print(bool(123))
print(bool(["Manzana, Pera"]))

# False

print(bool(""))
print(bool(0))
print(bool([]))
print(bool(None))

x = 123
print(isinstance(x, int))