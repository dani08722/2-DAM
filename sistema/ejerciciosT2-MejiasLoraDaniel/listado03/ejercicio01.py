recaudadoCadaDia=[]
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
            recaudadoCadaDia.append(recaudado)

        case 2:
            # • Poner a cero una recaudación (se me ha ido el cliente sin pagar). 
            for i in recaudadoCadaDia:
                print(" Recaudo día ",recaudadoCadaDia.index(i)+1,": ",i,"€")

            dia=int(input("Introduce el dia del recaudo que deseas poner a cero"))
            recaudadoCadaDia[dia-1]=0

        # • Imprimir toda la lista, es decir, mostrar todos los datos de todas las recaudaciones en bonito.
        case 3:
            for i in recaudadoCadaDia:
                print(" Recaudo día ",recaudadoCadaDia.index(i)+1,": ",i,"€")
                


        # • Buscar el día en que más he ganado y decir cuántos días he ganado esa cantidad. 
        case 4:
            dia=recaudadoCadaDia.index(max(recaudadoCadaDia))+1
            print("Día que mas he ganado: ",dia," ",max(recaudadoCadaDia),"€")
            print("Días que he ganado esa cantidad: ",recaudadoCadaDia.count(max(recaudadoCadaDia)))


        # • Sumar una cantidad a un día como gasto extra. 
        case 5:
            for i in recaudadoCadaDia:
                print(" Recaudo día ",recaudadoCadaDia.index(i)+1,": ",i,"€")
                
            dia=int(input("Introduce el dia del recaudo"))
            extra=float(input("Introduce la cantidad extra a añadir: "))
            recaudadoCadaDia[dia-1]+=extra

        # • Calcular cuánto he recaudado en todas las recaudaciones. 
        case 6:
            total=sum(recaudadoCadaDia)
            print("Recaudado total: ",total,"€")


        # • Ordenar la lista de mayor a menor. 
        case 7:
            recaudadoCadaDia.sort(reverse=True)

        # • Calcular la media diaria. 
        case 8:
            media=sum(recaudadoCadaDia)/len(recaudadoCadaDia)
            print("Media: ",round(media,2),"€")
        
        # • Calcular el porcentaje de días al mes (suponiendo 30 días) en que he tenido la habitación alquilada. 
        case 9:
            porcentaje=(len(recaudadoCadaDia)/30)*100
            print(f"Has tenido la habitación alquilada el {round(porcentaje),2}% del mes")
        # • Dividir la lista en dos nuevas listas. Una de ellas debe ser la que tenga las 5 menores recaudaciones, la otra las restantes. 
        case 10:
            ordenada=sorted(recaudadoCadaDia,reverse=True)
            menores=ordenada.copy()[-5:]
            restantes=recaudadoCadaDia.copy()[:-5]
            print("Menores recaudaciones: ",menores)
            print("Restantes: ",restantes)
