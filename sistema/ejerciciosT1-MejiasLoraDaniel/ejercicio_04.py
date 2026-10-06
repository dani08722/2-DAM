# Ejercicio 4: indicar cuál de dos números es mayor.

numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))

if numero1 > numero2:
    print("El mayor es", numero1)
elif numero2 > numero1:
    print("El mayor es", numero2)
else:
    print("Los dos números son iguales")