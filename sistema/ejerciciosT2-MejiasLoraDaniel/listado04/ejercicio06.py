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

f.close()

import random
SIGNOS = ".,;:!?\"'()"
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
            print("\n\nSaliendo del programa...\n\n")
        
        case 1:
            palabra_mayor = ""
            with open("ejerciciosT2-MejiasLoraDaniel/listado04/ficheros/entrada.txt", "r") as f:
                for linea in f:
                    for palabra in linea.split():
                        palabra_limpia = palabra.strip(SIGNOS)
                        if len(palabra_limpia) > len(palabra_mayor):
                            palabra_mayor = palabra

            print(f"\n\nLa palabra más larga es: '{palabra_mayor}' ({len(palabra_mayor)} letras).\n\n")

        case 2:
            palabra_contar=str(input("Introduzca la palabra a contar: ").strip().lower())
            contador=int(0)

            with open("ejerciciosT2-MejiasLoraDaniel/listado04/ficheros/entrada.txt", "r") as f:
                for linea in f:
                    for palabra in linea.split():
                        palabra_limpia = palabra.strip(SIGNOS).lower()
                        if palabra_limpia == palabra_contar:
                            contador+=1

            print(f"\n\nLa palabra {palabra_contar} ha aparecido {contador} veces en el texto\n\n")


        case 3:

            #minimo = 1
            #contador=0
            #with open("ejerciciosT2-MejiasLoraDaniel/listado04/ficheros/entrada.txt", "r") as f:
            
            #    for linea in f:
            #        contador+=1
            #    maximo = contador
            # linea_aleatoria = random.randint(minimo,maximo)

            #contador=1
            #f = open("ejerciciosT2-MejiasLoraDaniel/listado04/ficheros/entrada.txt", "r")
            #for linea in f:
            #    if linea_aleatoria==contador:
            #        print(linea)
            #    contador+=1
            with open("ejerciciosT2-MejiasLoraDaniel/listado04/ficheros/entrada.txt", "r") as f:
                lineas = f.readlines()

                if lineas:
                    linea_aleatoria = random.choice(lineas).strip()
                    print(f"\n\nLínea aleatoria: {linea_aleatoria}\n\n")
                else:
                    print("\n\nEl fichero está vacío\n\n")

        case 4:
            
            total_palabras=0
            with open("ejerciciosT2-MejiasLoraDaniel/listado04/ficheros/entrada.txt", "r") as f:
                for linea in f:
                    for palabra in linea.split():
                        total_palabras+=1

            print(f"\n\nEn el fichero hay un total de: {total_palabras} palabras\n\n")

        case 5:
            total_lineas=0

            with open("ejerciciosT2-MejiasLoraDaniel/listado04/ficheros/entrada.txt", "r") as f:

                for linea in f:
                    total_lineas+=1

            print(f"\n\nEl fichero tiene el total de: {total_lineas} lineas")
            

    