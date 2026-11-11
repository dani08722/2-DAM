# 5. Crea un conjunto de números enteros leyendo por teclado. Se podrá hacer lo siguiente:

# 1. Añadir el número 15.
# 2. Eliminar el número 9.
# 3. Calcular la cantidad de elementos.
# 4. Comprobar si 6 está en el conjunto.

numeros= set()
opcion=int(1999999)
cantidadNumeros=int(input("Introduce la cantidad de números que desea añadir: "))

for i in range(cantidadNumeros):
    numero=int(input(""))
    numeros.add(numero)

while opcion!=0:
    opcion=int(input("[1] Añadir número\n[2] Eliminar número\n[3] Calcular la cantidad de elementos\n"
    "[4] Comprobar si x número está\n[5] Mostrar conjunto\nIntroduce la opción: "))
    match opcion:
        case 0:
            print("Saliendo del programa")

        case 1:
            numero=int(input("Introduce el número que desea añadir: "))
            numeros.add(numero)

        case 2:
            numero=int(input("Introduce el número que desea eliminar: "))
            numeros.remove(numero)

        case 3:
            print("La cantidad de elementos es de: ",len(numeros))

        case 4:
            numero=int(input("Introduce el número que desea comprobar si está en el conjunto: "))
            comprobar=numero in numeros
            if comprobar:
                print("El número pertenece al conjunto")
            else:
                print("El número no pertenece al conjuntos")

        case 5:
            print(numeros)