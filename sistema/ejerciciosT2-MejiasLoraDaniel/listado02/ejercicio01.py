temperaturas=(21,24,19,30,25,28)


print("Temperatura máxima: ",max(temperaturas))
media=sum(temperaturas)/len(temperaturas)
print("La media es: ",media)
listaTemperaturas=list(temperaturas)
listaTemperaturas.append(60)
temperaturas= tuple(listaTemperaturas)
print(temperaturas)
if 31 in temperaturas:
    print("El número está en la tupla")
else:
    print("El número no está en la tupla")