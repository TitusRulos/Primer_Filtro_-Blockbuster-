def validar_opcion(enunciando,inferior,superior):
    while True:
        try:
            opcion =int(input(enunciando))
            if opcion>=inferior and opcion<=superior:
                return opcion
                break
            else:
                print(f"Opción no está entre el intervalo de ({inferior}-{superior})")
        except ValueError:
            print("Por favor, introduce un número válido. ")

def menu_principal():
    print("Sistema gestor de peliculas block buster:\n 1. Gestor de gèneros\n 2. Gestor de actores\n 3. Gestor de formatos\n 4. Gestor de informes\n 5. Gestor de peliculas\n 6. Salir")
    op=validar_opcion("Opcion: ", 1, 6)
    return op
def menu_generos():
    print("Gestionar genereos:\n 1. Crear genero\n 2. listar generos")
