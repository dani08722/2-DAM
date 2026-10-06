# Ejercicio 6: indicar en qué intervalo está el número.

numero = float(input("Introduce un número: "))

if 0 <= numero <= 10:
    print("El número está entre 0 y 10")
elif 11 <= numero <= 20:
    print("El número está entre 11 y 20")
elif 21 <= numero <= 30:
    print("El número está entre 21 y 30")
else:
    print("El número no está entre 0 y 30")