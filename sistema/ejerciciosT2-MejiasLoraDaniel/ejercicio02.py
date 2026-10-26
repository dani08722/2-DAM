# 2. Crear un programa que explique las distintas funcionalidades de Python usando listas. Puedes empezar con
# las típicas CRUD y hacerlo con una lista rellena directamente. Ejemplo: buscar, insertar al final o en una
# posición concreta, borrar, distintas formas de eliminar... Puedes seguir el orden del archivo de teoría.

# Crea un menú para que en cada case se vaya eligiendo lo que se quiere hacer.

# Cuando se termine debes hacer el enunciado y la solución de un ejercicio que utilice lo anterior. Debe estar
# contextualizado, es decir, que tenga enunciado real y aunque, puedes usar otras funciones funcionalidades de
# las listas, debe estar centrado en la que te ha estudiado en este apartado de listas de la teoría, por ejemplo, para
# explicar el borrado podemos usar el buscar el elemento a borrar. 

numeros = [0,1,2,3,4,5,6,7,8,9,10]
opcion=1000
while opcion!=0:
    print("Pulsa [0] para salir")
    print("Pulsa [1] para insertar en una posición concreta")
    print("Pulsa [2] para insertar al final de la lista")
    print("Pulsa [3] para buscar una posición de la lista")
    print("Pulsa [4] para mostrar la lista")
    print("Pulsa [5] para eliminar un número en concreto")
    print("Pulsa [6] para eliminar un número por índice")
    print("Pulsa [7] para eliminar toda la lista")
    print("Pulsa [8] para encontrar el índice de un número")
    print("Pulsa [9] para ver si un número esta en la lista")
    int(opcion=input("Selecciona una opción: "))

    match opcion:
        case 0:
            print("Saliendo del programa...")
            break
        case 1:
            index=input("Introduzca la posición de la lista que quieres insertar el número")
            numero=input("Introduce el número que desea insertar")
            numeros[numeros.insert(index,numero)]
        case 2:
            numero=input("Introduce el número que desea insertar")
            numeros.append(numero)
        case 3:
            index=input("Introduce la posición de la lista que quieres buscar")
            print(numeros[index])
        case 4:
            print(numeros)
        case 5:

        case 6:

        case 7:

        case 8:

        case 9:
