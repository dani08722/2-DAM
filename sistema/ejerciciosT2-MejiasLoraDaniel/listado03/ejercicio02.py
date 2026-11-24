# Estoy dando clases de inglés para el B2 y me gustaría que me ayudarais a crear un diccionario para ver cómo 
# se dicen palabras con significado “raro” españolas en inglés. Se hará todo en el mismo archivo, no se crean 
# clases. Por ejemplo, “Cabeza: (en el sur de España) amigo/colega”, aro: sí, de acuerdo. Consideraremos que 
# no se repiten palabras con el mismo nombre, es decir, que la palabra “take” no aparece dos veces en el 
# diccionario y que, si tiene varios significados, estos pueden ir en el mismo String “significado”, por ejemplo, 
# for---->por, para, durante. 
# Se debe utilizar un diccionario que se puede instanciar con algunos elementos de inicio y un menú para cada 
# uno de las siguientes funcionalidades: 
diccionario={
    "Cabeza": "Amigo, colega (sur de España)",
    "Aro": "Sí, de acuerdo",
    "For": "Por, para, durante"
}

# • Agregar una nueva palabra por teclado. 

opcion=int(1000000)
while opcion!=0:
    opcion=int(input("[0] Salir\n[1] Agregar nueva palabra\n[2] Ver diccionario completo\n[3] Buscar una palabra\n"
    "[4] Modificar significado de una palabra\n[5] Añadir dos palabras favoritas\n"
    "[6] Borrar una palabra\n[7] Ordenar diccionario alfabéticamente\nSeleccione una opción: "))

    match opcion:
        case 0:
            print("Saliendo del programa...")

        case 1:
            # Agregar una nueva palabra.
            palabra=str(input("Introduce la palabra: "))
            significado=str(input("Introduce el significado: "))
            diccionario[palabra]=significado

        case 2:
            # Imprimir el diccionario completo en bonito.
            for palabra,significado in diccionario.items():
                print(f"{palabra}, significa: {significado}")

        case 3:
            # Buscar una palabra por nombre.
            palabra=str(input("Introduce la palabra: "))
            if palabra in diccionario:
                print(diccionario[palabra])
            else:
                print("La palabra no se encuentra en el diccionario.")

        case 4:
            # Modificar el significado de una palabra.
            palabra=str(input("Introduce la palabra que deseas modificar: "))
            if palabra in diccionario:
                significado=str(input("Introduce el nuevo significado: "))
                diccionario[palabra]=significado
            else:
                print("La palabra no se encuentra en el diccionario.")

        case 5:
            # Añadir dos palabras favoritas y combinarlas con el diccionario.
            for i in range(2):
                palabra=input("Introduce tu palabra favorita en inglés: ")
                significado=input("Introduce su significado: ")
                diccionario[palabra]=significado

        case 6:
            # Borrar una palabra.
            palabra=str(input("Introduce la palabra que deseas eliminar: "))
            if palabra in diccionario:
                del diccionario[palabra]
                print("Palabra eliminada correctamente")
            else:
                print("La palabra no se encuentra en el diccionario")
        case 7:
            # Ordenar el diccionario alfabéticamente.
            diccionario=dict(sorted(diccionario.items()))

        case _:
            print("Opción no válida.")