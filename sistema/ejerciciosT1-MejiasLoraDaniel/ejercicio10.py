numeros = []
numero = input("Introduce un número entero (Enter para terminar): ")

while numero != "":
    numeros.append(int(numero))
    numero = input("Introduce otro número entero (Enter para terminar): ")

print("Números introducidos:", numeros)