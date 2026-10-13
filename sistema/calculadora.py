import time

opcion=int(1)
while opcion != 0:
    print("\n\n\n\n\nPulsa [0] para salir")
    print("Pulsa [1] para sumar")
    print("Pulsa [2] para restar")
    print("Pulsa [3] para multiplicar")
    print("Pulsa [4] para dividir")
    opcion= int(input("Introduce la opcion: "))
    match opcion:
        case int(0):
            print("Fin del programa")
            break
        case int(1):
            print("Suma")
            num1= float(input("Introduce el primer número: "))
            num2= float(input("Introduce el segundo número: "))
            resultado= num1 + num2
            print("-------------------------------------")
            print("El resultado es: ",resultado)
            print("-------------------------------------")
            time.sleep(2)
        case int(2):
            print("Resta")
            num1= float(input("Introduce el primer número: "))
            num2= float(input("Introduce el segundo número: "))
            resulado= num1 - num2
            print("-------------------------------------")
            print("El resultado es: ", resulado)
            print("-------------------------------------")
            time.sleep(2)
        case int(3):
            print("Multiplicación")
            num1= float(input("Introduce el primer número: "))
            num2= float(input("Introduce el segundo número: "))
            resulado= num1 * num2
            print("-------------------------------------")
            print("El resultado es: ", resulado)
            print("-------------------------------------")
            time.sleep(2)
        case int(4):
            print("Division")
            num1= float(input("Introduce el dividendo: "))
            num2= float(input("Introduce el divisor: "))
            resulado= num1 / num2
            print("-------------------------------------")
            print("El resultado es: ", resulado)
            print("-------------------------------------")
            time.sleep(2)