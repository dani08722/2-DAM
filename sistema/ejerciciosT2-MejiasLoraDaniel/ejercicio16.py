import random
opcion="100"

tempMin=float(input("Introduzca el minimo: "))
tempMax=float(input("Introduzca el máximo: "))
diasGenerar= int(input("Introduzca la cantidad de días para generar: "))
suma=int(0)

listaTemperaturas=[]

for i in range(diasGenerar):
    aleatorio= round(random.uniform(tempMin,tempMax),2)
    listaTemperaturas.append(aleatorio)

while opcion!="0":

    print("\n\n[0] Salir del programa")
    print("[1] Mostrar todas las temperaturas")
    print("[2] Calcular y mostrar media")
    print("[3] Mostrar temperatura mínima y máxima")
    print("[4] Ordenar la lista de mayor a menor")
    print("[5] Mostrar cuántos días tuvieron temperaturas por encima de la media")
    print("[6] Crear una nueva lista solo con las temperaturas superiores a la media\n")

    opcion=input("Introduzca la opcion: ")
    match opcion:
        case "0":
            print("\n\nSaliendo del programa:")
            break

        case "1":
            print("\n\n",listaTemperaturas)

        case "2":
            contador=0
            suma=0

            for temperatura in listaTemperaturas:
                suma = suma + temperatura
                contador += 1

            media=suma/contador
            print("\n\n",round(media,2))

            suma=sum(listaTemperaturas)
            media=suma/len(listaTemperaturas)
            print(media)

        case "3":
            minimaTemp=min(listaTemperaturas)
            maximaTemp=max(listaTemperaturas)
            print("\n\nDía: ",listaTemperaturas.index(minimaTemp)+1," ",minimaTemp)
            print("Día: ",listaTemperaturas.index(maximaTemp)+1," ",maximaTemp)

        case "4":
            listaTemperaturas.sort(reverse=True)
            print("\n\nLista ordenada!!")

        case "5":
            contador=0
            media=0

            for temperatura in listaTemperaturas:
                suma = suma + temperatura
                contador += 1

            media=suma/contador

            contador=0
            for temperatura in listaTemperaturas:
                if temperatura>media:
                    contador += 1

            print("\n\n",contador, " Días tuvieron temperatura mayor a la media")

        case "6":
            suma=sum(listaTemperaturas)
            media=suma/len(listaTemperaturas)
            listaTemperaturasMayorMedia=[]
            
            for temperatura in listaTemperaturas:
                if temperatura > media:
                    listaTemperaturasMayorMedia.append(temperatura)

            print(listaTemperaturasMayorMedia)