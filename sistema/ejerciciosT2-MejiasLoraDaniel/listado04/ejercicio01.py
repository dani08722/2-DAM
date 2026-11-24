# Escribe un programa que cuente cuántas líneas NO vacías contiene un fichero 'entrada.txt' que tenga varias líneas de prueba. 

f = open("ejerciciosT2-MejiasLoraDaniel/listado04/ficheros/entrada.txt", "w")
f.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry.\n" 
"Lorem Ipsum has been the industry's standard dummy text ever since 1966,\n "
"when designers at Letraset and James Mosley, the librarian at St Bride Printing Library in London,\n "
"took a 1914 Cicero translation and scrambled it to make dummy text for Letraset's Body Type sheets.\n "
"It has survived not only many decades, but also the leap into electronic typesetting,\n "
"remaining essentially unchanged. It was popularised thanks to these sheets and more\n "
"recently with desktop publishing software like Aldus PageMaker and Microsoft\n "
"Word including versions of Lorem Ipsum.")

contador=0
f = open("ejerciciosT2-MejiasLoraDaniel/listado04/ficheros/entrada.txt", "r")

for linea in f:
    contador+=1

print(contador)