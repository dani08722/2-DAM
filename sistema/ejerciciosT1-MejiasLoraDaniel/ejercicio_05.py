# Ejercicio 5: Crea una variable numérica y si está entre 0 y 10, mostrar un mensaje indicándolo.

numero = float(input("Introduce un número: "))

if 0 <= numero <= 10:
    print("El número está entre 0 y 10")
else:
    print("El número no está entre 0 y 10")