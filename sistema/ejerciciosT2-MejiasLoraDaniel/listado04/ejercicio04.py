# Crea un programa que lea un fichero llamado 'texto.txt' y genere 'numerado.txt' con todas las líneas precedidas de su número

f = open("ejerciciosT2-MejiasLoraDaniel/listado04/ficheros/entrada.txt", "w")
f.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry.\n" 
"Lorem Ipsum has been the industry's standard dummy text ever since 1966,\n "
"when designers at Letraset and James Mosley, the librarian at St Bride Printing Library in London,\n "
"took a 1914 Cicero translation and scrambled it to make dummy text for Letraset's Body Type sheets.\n "
"It has survived not only many decades, but also the leap into electronic typesetting,\n "
"remaining essentially unchanged. It was popularised thanks to these sheets and more\n "
"recently with desktop publishing software like Aldus PageMaker and Microsoft\n "
"Word including versions of Lorem Ipsum.")

f = open("ejerciciosT2-MejiasLoraDaniel/listado04/ficheros/entrada.txt", "r")
f2 = open("ejerciciosT2-MejiasLoraDaniel/listado04/ficheros/copia.txt", "w")

contador=1

for linea in f:
    f2.write("Línea: "+str(contador) + " " + linea)
    contador+=1

f2= open("ejerciciosT2-MejiasLoraDaniel/listado04/ficheros/copia.txt", "r")
for linea in f2:
    print(linea)