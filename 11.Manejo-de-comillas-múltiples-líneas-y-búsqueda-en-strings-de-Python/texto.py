print("Hola 'mundo'")
print('Hola "mundo"')

ingles = "I'm Dave"

multiples = """Hola
Mundo!
Desde
Las
Comillas
Triples"""

print(ingles)
print(multiples)

palabra = "Murcielago"
print(len(palabra))

texto = "Este curso es de fundamentos de python"
estaIncluida = "python" in texto
noEstaIncluida = "javascript" not in texto

print(estaIncluida)
print(noEstaIncluida)

mayuscula = texto.upper()
print(mayuscula)

minuscula = texto.lower()
print(minuscula)

texto2 = texto.upper()
texto2 = texto.lower()

print(texto2) # Siempre toma el ultimo resultado
 
espacios = "     Este es el texto     "
sinEspacios = espacios.strip()
print(sinEspacios)