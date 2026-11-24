recaudaciones=[5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0, 45.0, 50.0]
contador=0
opcion=int(1000000)
while opcion!=0:
    opcion=int(input("[0] Salir\n[1] Agregar nueva recaudacion\n[2] Poner a cero una recaudación(se me ha ido el cliente sin pagar)" \
    "\n[3] Ver lista\n[4] Buscar día que más he ganado y cuántos días he ganado esa cantidad\n[5] Sumar extra a un recaudo\n[6] Calcular total\n" \
    "[7] Ordenar de mayor a menor\n[8] Calcular media\n[9] Calcular porcentaje de días al mes que he tenido la habitación alquilada\n" \
    "[10] Dividir en dos listas(5 menores recaudaciones/restantes)\nSelecione una opción: "))

    match opcion:
        case 0:
            print("Saliendo del programa...")

        case 1:
            # Agregar una nueva recaudación. 
            recaudado=float(input("Introduce lo recaudado el día de hoy: "))
            recaudaciones.append(recaudado)

        case 2:
            # • Poner a cero una recaudación (se me ha ido el cliente sin pagar). 
            for i in recaudaciones:
                print(" Recaudo día ",recaudaciones.index(i)+1,": ",i,"€")

            dia=int(input("Introduce el dia del recaudo que deseas poner a cero"))
            recaudaciones[dia-1]=0

        # • Imprimir toda la lista, es decir, mostrar todos los datos de todas las recaudaciones en bonito.
        case 3:
            for i in recaudaciones:
                print(" Recaudo día ",recaudaciones.index(i)+1,": ",i,"€")
                


        # • Buscar el día en que más he ganado y decir cuántos días he ganado esa cantidad. 
        case 4:
            mayor=max(recaudaciones)
            print("Día que mas he ganado: ",recaudaciones.index(mayor)+1," ",mayor,"€")
            print("Días que he ganado esa cantidad: ",recaudaciones.count(mayor))


        # • Sumar una cantidad a un día como gasto extra. 
        case 5:
            for i in recaudaciones:
                print(" Recaudo día ",recaudaciones.index(i)+1,": ",i,"€")
                
            dia=int(input("Introduce el dia del recaudo"))
            extra=float(input("Introduce la cantidad extra a añadir: "))
            recaudaciones[dia-1]+=extra

        # • Calcular cuánto he recaudado en todas las recaudaciones. 
        case 6:
            total=sum(recaudaciones)
            print("Recaudado total: ",total,"€")


        # • Ordenar la lista de mayor a menor. 
        case 7:
            recaudaciones.sort(reverse=True)
            print("Lista ordenada de mayor a menor: ")
            print(recaudaciones)

        # • Calcular la media diaria. 
        case 8:
            media=sum(recaudaciones)/len(recaudaciones)
            print("Media: ",round(media,2),"€")
        
        # • Calcular el porcentaje de días al mes (suponiendo 30 días) en que he tenido la habitación alquilada. 
        case 9:
            porcentaje=(len(recaudaciones)/30)*100
            print(f"Has tenido la habitación alquilada el {round(porcentaje),2}% del mes")
        # • Dividir la lista en dos nuevas listas. Una de ellas debe ser la que tenga las 5 menores recaudaciones, la otra las restantes. 
        case 10:
            ordenada=sorted(recaudaciones,reverse=True)
            menores=ordenada.copy()[-5:0]
            restantes=recaudaciones.copy()[0:-5]
            print("Menores recaudaciones: ",menores)
            print("Restantes: ",restantes)
