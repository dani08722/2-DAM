# Los conjuntos tambien se pueden crear por comprension.
# La expresion se parece a la comprension de listas, pero usa llaves.
# En este ejemplo guardamos los multiplos de 3 entre 0 y 19.

multiplos_de_3 = {numero for numero in range(0, 20) if numero % 3 == 0}

print(multiplos_de_3)
# El orden al mostrar un conjunto puede variar, porque los conjuntos no tienen orden.
