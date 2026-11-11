# 3. Crear un diccionario que tenga como claves el dni de un estudiante y como valor la nota media de su
# expediente. La nota media se generará de manera aleatoria entre 1 y 10.
# Escribir el código necesario en un menú para hacer los siguiente:
# a) Mostrar los datos.
# b) Modificar la nota.
# c) Añadir un nuevo estudiante.
# d) Crear un nuevo diccionario (no modificar el original) solo con los estudiantes que tienen nota media
# mayor a un valor dado por teclado (por ejemplo, para comprobar que pueden entrar en un ciclo según esa
# nota de corte).

from copy import deepcopy
import random
opcion=int(100000)

notaMedia=random.uniform(1.0,10.0)
estudiante={"30315692J":notaMedia}

while opcion!=int(0):
    opcion=int(input("[1] Para mostrar los datos\n[2] Para modificar la nota\n[3] Para añadir un nuevo estudiante\n"
    "[4] Para crear un nuevo diccionario con nota media mayor a:\nIntroduce la opcion: "))
    match opcion:
        case int(0):
            print("Saliendo del programa")
        
        case int(1):
            print(estudiante)

        case int(2):
            valor=str(input("Introduce el dni del estudiante: "))
            if valor in estudiante:

                notaMediaNueva=float(input("Introduce la nueva nota media: "))
                estudiante[valor]=notaMediaNueva
            else:   
                print("No hay ningun estudiante con ese dni")

        case int(3):
            valor=str(input("Introduce el dni del nuevo estudiante: "))
            if valor not in estudiante:
                notaMedia=float(input("Introduce la nota media: "))
                estudiante[valor]=notaMedia
            else:
                print("Ya hay un estudiante registrado con ese dni")

        case int(4):
            copiaEstudiantes=estudiante.copy()
            notaCorte=float(input("Introduce la nota de corte: "))
            copiaEstudiantes={dni:media for dni,media in copiaEstudiantes.items() if media>=notaCorte}
            print(copiaEstudiantes)