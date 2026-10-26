# Haga un programa de la interfaz de un cajero automático. Tendrá las opciones, ver saldo,
# retirar dinero, comprar entradas e ingresar dinero. En cada opción se pedirán los datos
# necesarios y se realizarán las operaciones adecuadas. El coste de las entradas se debe restar al
# saldo de dicha cuenta. La cuenta será creada por nosotros con un saldo inicial concreto.


saldo=float(input("Introduzca el saldo inicial: "))
precio_entrada=30.0
opcion=1
while opcion!=0:
    print("Salir [0]")
    print("Ver saldo [1]")
    print("Retirar dinero [2]")
    print("Comprar entradas [3]")
    print("Ingresar dinero [4]")
    opcion=int(input("Introduce la opcion: "))
    match opcion:
        case 0:
            print("Gracias por utilizar el programa")
            break
        case 1:
            print("El saldo actual es: ",saldo)
        case 2:
            retirar=float(input("Saldo a retirar: "))
            saldo -= retirar
        case 3:
            print("Entrada concierto shakira 30$")
            cantidad_entradas=int(input("Introduzca la cantidad de entradas a comprar deseadas: "))
            if (cantidad_entradas*precio_entrada) > saldo:
                print("No hay suficiente saldo en la cuenta")
            else:
                saldo-=cantidad_entradas*precio_entrada
                print("Entradas compradas")
        case 4:
            ingresar=float(input("Introduzca el dinero a ingresar: "))
            saldo+=ingresar
