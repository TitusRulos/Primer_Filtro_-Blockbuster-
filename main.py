from consola.menus import menu_principal, menu_actores, menu_formatos, menu_generos, menu_informes, menu_peliculas
from funciones.blockbuster import crear_genero, leer_lista_generos, crear_actor, leer_lista_actores, crear_formato, leer_lista_formatos, crea_pelicula

while True:
    print()
    op=menu_principal()

    if op== 1:
        print()
        op=menu_generos()
        if op==1:
            crear_genero()
            op=0
        if op==2:
            leer_lista_generos()
            op=0
        if op==3:
            print("Saliendo al menu principal")
            op=0

    if op== 2:
        print()
        op=menu_actores()
        if op==1:
            crear_actor()
            op=0
        if op==2:
            leer_lista_actores()
            op=0
        if op==3:
            print("Saliendo al menu principal")
            op=0

    if op== 3:
        print()
        op=menu_formatos()
        if op==1:
            crear_formato()
            op=0
        if op==2:
            leer_lista_formatos()
            op=0
        if op==3:
            print("Saliendo al menu principal")
            op=0

    if op== 4:
        print()
        op=0
        op=menu_informes()
        if op==1:
            print()
            op=0
        if op==2:
            print()
            op=0
        if op==3:
            print("Saliendo al menu principal")
            op=0

    if op== 5:
        print()
        op=menu_peliculas()
        if op==1:
            crea_pelicula()
            op=0
        if op==2:
            print()
            op=0
        if op==3:
            print()
            op=0
        if op==4:
            print()
            op=0
        if op==5:
            print()
            op=0
        if op==6:
            print()
            op=0
        if op==7:
            print("Saliendo al menu principal")
            op=0
            
    if op== 6:
        print()
        print("Saliendo")
        break


    
    