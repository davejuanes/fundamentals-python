# open(nombre, modo)

# R (read) Lectura
# W (write) Escritorio
# X (crea archivo nuevo) Lectura

try:
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.readline())
        print(f.readline())
    
    """ f = open("archivo.txt", "r")
    print(f.readline())
    f.close() """
except FileNotFoundError:
    open("archivo.txt", "x")
    print("No se ha encontrato el archivo")

try:
    with open("archivo.txt", "a") as f:
        f.write("\n")
        f.write("Hola mundo desde el write en el with")
    with open("archivo.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("No se ha encontrato el archivo")