objetivo = int(input("Introduce el número que quieres alcanzar: "))
numeros = []
suma = 0

while suma != objetivo:
    numero = int(input("Introduce un número entero: "))
    numeros.append(numero)
    suma += numero

print("La suma coincide con el número inicial.")
print("Lista de números:", numeros)