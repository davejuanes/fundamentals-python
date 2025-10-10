# Lambda es una funcion pequeña y anonima que puede tener muchos argumentos pero solo una expresion

# Sintaxis lambda argumentos : expresion

# x = lambda a : a + 10
x = lambda a, b : a + b

print(x(5, 2))

def mi_funcion(n):
    return lambda a : a * n

duplicador = mi_funcion(2)
triplicador = mi_funcion(3)

print(duplicador(5))
print(triplicador(5))