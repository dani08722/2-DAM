# Crea un programa que lea de un fichero y tenga las siguientes funcionalidades en un menú: 

# - La palabra de mayor longitud. 
# - Las veces que aparece una palabra. 
# - Lea una línea aleatoria del fichero. 
# - Dos funcionalidades más inventadas por tí. 

f = open("ejerciciosT2-MejiasLoraDaniel/listado04/ficheros/entrada.txt", "w")
f.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry.\n" 
"Lorem Ipsum has been the industry's standard dummy text ever since 1966,\n "
"when designers at Letraset and James Mosley, the librarian at St Bride Printing Library in London,\n "
"took a 1914 Cicero translation and scrambled it to make dummy text for Letraset's Body Type sheets.\n "
"It has survived not only many decades, but also the leap into electronic typesetting,\n "
"remaining essentially unchanged. It was popularised thanks to these sheets and more\n "
"recently with desktop publishing software like Aldus PageMaker and Microsoft\n "
"Word including versions of Lorem Ipsum.")


opcion = int(10000)

while opcion != 0:
    print("1. La palabra de mayor longitud.")
    print("2. Las veces que aparece una palabra.")
    print("3. Lea una línea aleatoria del fichero.")
    print("4. Contar cuántas palabras hay en el fichero.")
    print("5. Contar cuántas líneas hay en el fichero.")
    print("0. Salir del programa.")

    opcion = int(input("Elige una opción: "))
    match opcion:
        case 0: 
            print("Saliendo del programa...")
        
        case 1:
            f = open("ejerciciosT2-MejiasLoraDaniel/listado04/ficheros/entrada.txt", "r")
            palabra_mayor = "a"
            for linea in f:
                for palabra in linea.split():
                    if len(palabra)>len(palabra_mayor):
                        palabra_mayor=palabra

            print(palabra_mayor)

        case 2:
            f = open("ejerciciosT2-MejiasLoraDaniel/listado04/ficheros/entrada.txt", "r")
            palabra_contar="dummy"
            contador=int(0)
            for linea in f:
                for palabra in linea.split():
                    if palabra == palabra_contar:
                        contador+=1
            print(f"La palabra {palabra_contar} a aparecido {contador} veces en el texto")


    