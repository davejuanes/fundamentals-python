x = 5
y = 3
z = 10

if x > y or x > z:
    print("X es mayor a Y y X es menor a Z")
elif x == y:
    print("X es igual Y")
else:
    print("Ninguna de la condiciones anteriores se cumplió")

a = "Python"
b = "Javascript"
c = "Python"

if a == c:
    if a == b:
        print("a es igual a c pero es distinto de b")
    else:
        print("Estoy saliendo por el else del if interno")
else:
    print("A no es igual a B")


e = 10
f = 10

if e == f:
    # Nose que hacer si estas dos variables no son iguales
    pass # Para ignorar la estructura if hasta que se defina el comportamiento que se espera
