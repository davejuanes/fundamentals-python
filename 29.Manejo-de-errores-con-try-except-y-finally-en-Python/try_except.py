from ast import Name


try:
    # print("Intentamos algo")
    numero = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir por 0")

try:
    print(x)
except NameError:
    print("Esta variable nose ha definido")
finally:
    print("Esto sera ejecutado siendo exitoso o no el bloque")