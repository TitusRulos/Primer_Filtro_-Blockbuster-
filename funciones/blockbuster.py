import json
import os

lista_generos = []
lista_actores = []
lista_formatos = []
lista_peliculas = []

def crear_genero():
    
    id_genero=input("id: ")
    nombre_genero=input("nombre del genero:")
    genero = {
        'id': id_genero,
        'nombre': nombre_genero
    }
    
    lista_generos.append(genero)

    try:
        with open(os.path.join("data", "generos.json"), 'w') as archivo_json:
            json.dump(lista_generos, archivo_json, indent=2)
            print("El genero ha sido guardado exitosamente")
    except Exception as e:
        print(f"Error al guardar el genero: {e}")

def leer_lista_generos():
    print("Lista de generos: ")
    for gen in lista_generos:
        print(gen)
        print()
        
def crear_actor():
    id_actor=input("id: ")
    nombre_actor=input("nombre del genero:")
    actor = {
        'id': id_actor,
        'nombre': nombre_actor
    }
    
    lista_actores.append(actor)

    try:
        with open(os.path.join("data", "actores.json"), 'w') as archivo_json:
            json.dump(lista_actores, archivo_json, indent=2)
            print("El actor ha sido guardado exitosamente")
    except Exception as e:
        print(f"Error al guardar el actor: {e}")

def leer_lista_actores():
    print("Lista de actores: ")
    for act in lista_actores:
        print(act)
        print()

def crear_formato():
    id_formato=input("id: ")
    nombre_formato=input("nombre del formato:")
    formato = {
        'id': id_formato,
        'nombre': nombre_formato
    }
    
    lista_formatos.append(formato)

    try:
        with open(os.path.join("data", "formatos.json"), 'w') as archivo_json:
            json.dump(lista_formatos, archivo_json, indent=2)
            print("El formato ha sido guardado exitosamente")
    except Exception as e:
        print(f"Error al guardar el formato: {e}")

def leer_lista_formatos():
    print("Lista de formatos: ")
    for format in lista_formatos:
        print(format)
        print()

def crea_pelicula():

    id_pelicula=input("id: ")
    nombre_pelicula=input("nombre del genero: ")
    duracion= input("duracion: ")
    sinopsis= input("sinopsis: ")
    print()
    leer_lista_generos()
    print()
    try:
        generos_pelicula=int(input())
        for i in lista_generos:
            if generos_pelicula == i:
                pelicula = {
                'id': id_pelicula,
                'nombre': nombre_pelicula,
                'duracion': duracion,
                'sinopsis': sinopsis,
                'genero(s)': generos_pelicula
                }
                lista_peliculas.append(pelicula)
    except ValueError:
        print("No existe ese genero")
    try:
        with open(os.path.join("data", "peliculas.json"), 'w') as archivo_json:
            json.dump(lista_generos, archivo_json, indent=2)
            print("La pelicula ha sido guardado exitosamente")
    except Exception as e:
        print(f"Error al guardar la pelicula: {e}")
                
            

    
