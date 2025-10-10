from menu import mostrar_menu

def main():
    while True:
        # Mostrar el menu
        mostrar_menu()
        opcion = input("Selecciona un opción: ")

        if opcion == "1":
            #pedir un cafe
            pass
        elif opcion == "2":
            # historial
            pass
        elif opcion == "3":
            print("\n Muchas gracias por haber tomado nuestro cafés")
            break
        else:
            print("Opción inválida, por favor indique una de las opciones sugeridas")

if __name__ == "__main__": # Toma el nombre del archivo para ejecutar el archivo principal de manera obligatoria
    main()