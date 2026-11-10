# 3. Se quiere realizar un programa que lea por teclado las distintas notas obtenidas por un alumno 
# (comprendidas entre 0 y 10). A continuación, debe mostrar todas las notas a modo boletín de calificaciones, 
# la nota media, la nota más alta que ha sacado, la menor y el número de suspensos. 
notas=[]
suspensos=int(0)

cantidad= int(input("Introduce la cantidad de notas que quiere introducir: "))
contador=int(0)
while contador < cantidad:
    nota=float(input("Introduce la nota: "))
    if nota<0 or nota>10:
        print("La nota no es válida")
    else:
        notas.append(nota)
        contador += 1

media=sum(notas)/len(notas)

for nota in notas:
    if nota<5:
        suspensos +=1

print("Notas: ",notas)
print("Nota media: ",round(media,2))
print("La nota más alta es: ",max(notas))
print("La nota más baja es: ",min(notas))
print("Notas suspensas: ",suspensos)