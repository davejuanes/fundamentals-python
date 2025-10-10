ARCHIVO_PEDIDO = "pedidos.txt"

def ver_historial():
    try:
        print("\n Historial de pedidos")
        with open(ARCHIVO_PEDIDO, "r", encoding="UTF-8") as archivo:
            pedidos = archivo.readlines()
            if pedidos:
                for i, pedido in enumerate(pedidos, start=1):
                    print(str(i) + ". " + pedido.strip())
            else:
                print("\n Aún no hay ningún pedido")
    except FileNotFoundError:
        print("\n Todabía no existe un  historial de pedidos")