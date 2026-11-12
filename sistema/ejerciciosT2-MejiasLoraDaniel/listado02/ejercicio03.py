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

estudiante={"30315692J":round(random.uniform(1.0,10.0),2),
            "30315692A":round(random.uniform(1.0,10.0),2),
            "30315692B":round(random.uniform(1.0,10.0),2)}

while opcion!=int(0):
    opcion=int(input("[0] Para salir\n[1] Para mostrar los datos\n[2] Para modificar la nota\n[3] Para añadir un nuevo estudiante\n"
    "[4] Para crear un nuevo diccionario con nota media mayor a:\nIntroduce la opcion: "))
    match opcion:
        case 0:
            print("Saliendo del programa...")
        
        case 1:
            print(estudiante)
            print("DATOS DE LOS ESTUDIANTES")
            for dni,media in estudiante.items():
                print("DNI: ",dni," MEDIA: ",media)

        case 2:
            valor=str(input("Introduce el dni del estudiante: "))
            if valor in estudiante:

                notaMediaNueva=float(input("Introduce la nueva nota media: "))
                estudiante[valor]=notaMediaNueva
            else:   
                print("No hay ningun estudiante con ese dni")

        case 3:
            valor=str(input("Introduce el dni del nuevo estudiante: "))
            if valor not in estudiante:
                notaMedia=float(input("Introduce la nota media: "))
                estudiante[valor]=notaMedia
            else:
                print("Ya hay un estudiante registrado con ese dni")

        case 4:
            copiaEstudiantes=estudiante.copy()
            notaCorte=float(input("Introduce la nota de corte: "))
            copiaEstudiantes={dni:media for dni,media in copiaEstudiantes.items() if media>=notaCorte}
            print(copiaEstudiantes)