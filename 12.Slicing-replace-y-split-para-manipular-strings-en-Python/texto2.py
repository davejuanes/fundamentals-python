# Indi 0 1 2 3 4 5
texto = "Esto es un texto"

print(texto[4])
print(texto[:7])
print(texto[4:])
print(texto[5:-2])

curso = "Este es un curso de Javascript, Javascript"
print(curso.replace("Javascript", "Python"))

textoDividido = texto.split(" ")
print(textoDividido)

# Normalizacion

texto2 = "Este texto tiene MAYUSCULAS y minusculaes y necesito encontrar ciertas palabras"
print("mayusculas".lower() in texto2.lower())