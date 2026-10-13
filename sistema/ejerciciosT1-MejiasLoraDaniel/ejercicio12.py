# Escribe un programa que genere un número aleatorio entre 0 y 10 y nos pida adivinarlo Tenemos 3 intentos. 
# Puedes mirar el tutorial inicial de Python que usamos para instalar VS Code e instalar la biblioteca numpy.

import random

numero_aleatorio= random.randint(0,10)
intentos=0

while intentos < 3:
    numero= int(input("Adivina el numero entre 0 y 10: "))
    print(numero_aleatorio)
    if numero==numero_aleatorio:
        print("Has acertado")
        print("El número era: ",numero_aleatorio)
        break
    else:
        print("No has acertado")
        intentos += 1

print("El número era: ",numero_aleatorio)