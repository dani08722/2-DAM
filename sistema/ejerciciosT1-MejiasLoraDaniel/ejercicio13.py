def factorial(numero):
    resultado = 1

    for valor in range(1, numero + 1):
        resultado *= valor

    return resultado


numero = int(input("Introduce un número entero: "))

if numero < 0:
    print("No se puede calcular el factorial de un número negativo.")
else:
    print("El factorial de", numero, "es", factorial(numero))