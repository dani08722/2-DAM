def triangulo(numero):
    for fila in range(1, numero + 1):
        print("* " * fila)

    for fila in range(numero - 1, 0, -1):
        print("* " * fila)


triangulo(5)