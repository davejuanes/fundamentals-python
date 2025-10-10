# Funcion: es un bvloque de codigo que solo se ejecuta cuando lo llamamos. Permiten organizar y modularizar el codigo(rehutilizar)

def saludar(nombre, nacionalidad="Boliviano"): # Argumentos
    print("Hola", nombre, "de nacionalidad", nacionalidad)

# saludar("Dave", "Juanes") # Parametros
# saludar("Carla") # Parametros

def sumar(a, b):
    return a + b

resultado = sumar(5, 5)
print(resultado)

def funcion():
    pass

def calculos(operacion, a, b):
    if operacion == "suma":
        return (f"La {operacion} de {a} + {b} es {a+b}")
    if operacion == "resta":
        return (f"La {operacion} de {a} - {b} es {a-b}")
    if operacion == "multiplicacion":
        return (f"La {operacion} de {a} x {b} es {a*b}")
    if operacion == "division":
        return (f"La {operacion} de {a} / {b} es {a/b}")
    
resultado = calculos("resta", 5, 7)
print("Tu operación es", resultado)