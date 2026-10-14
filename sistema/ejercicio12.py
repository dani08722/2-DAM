import random

numero_secreto = random.randint(0, 10)
intentos = 3

while intentos > 0:
    numero = int(input("Adivina el número entre 0 y 10: "))

    if numero == numero_secreto:
        print("¡Has acertado!")
        break

    intentos -= 1
    if intentos > 0:
        print("No has acertado. Te quedan", intentos, "intentos.")
    else:
        print("Se han acabado los intentos. El número era", numero_secreto)