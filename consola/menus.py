def validar_opcion(enunciando,inferior,superior):
    while True:
        try:
            op =int(input(enunciando))
            if op>=inferior and op<=superior:
                return op
            else:
                print(f"Opción no está entre el intervalo de ({inferior}-{superior})")
        except ValueError:
            print("Por favor, introduce un número válido. ")
        break

def menu_principal():
    print("Sistema gestor de peliculas block buster: \n 1. Gestor de gèneros\n 2. Gestor de actores\n 3. Gestor de formatos\n 4. Gestor de informes\n 5. Gestor de peliculas\n 6. Salir")
    op=validar_opcion("Opcion: ", 1, 6)
    return op

def menu_generos():
    print("Gestionar genereos: \n 1. Crear genero\n 2. listar generos\n 3. Ir a menu principal")
    op=validar_opcion("Opcion: ", 1, 3)
    return op

def menu_actores():
    print("Gestionar actores: \n 1. Crear actor\n 2. Listar actor\n 3. Ir a menu principal")
    op=validar_opcion("Opcion: ", 1, 3)
    return op

def menu_formatos():
    print("Gestionar formatos: \n 1. Crear formatos\n 2. Listar formatos\n 3. Ir a menu principal")
    op=validar_opcion("Opcion: ", 1, 3)
    return op

def menu_informes():
    print("Gestionar informes: \n 1. Listar las peliculas de un genero específico \n 2. Listar las peliculas donde el protagonista sea Silvester Stallone\n 3. Buscar pelicula y mostrar sinopsis y los actores \n 4. Ir a menu principal")
    op=validar_opcion("Opcion: ", 1, 4)
    return op

def menu_peliculas():
    print("Gestionar películas:\n 1. Agregar peliculas\n 2. Editar pelicula\n 3. Eliminar pelicula\n 4. Eliminar actor\n 5. Buscar pelicula\n 6. Listar todas las peliculas\n 7. Ir a menu principal")
    op=validar_opcion("Opciom: ", 1, 7)
    return op





