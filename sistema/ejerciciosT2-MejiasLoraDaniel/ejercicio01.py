# Escribe un programa que defina una lista de números (positivos y negativos) y reemplace los números
# negativos por 0

numeros = [1,3,5,-1,-3,-5,0]
for i in numeros:
    if i<0:
        numeros[numeros.index(i)] = 0

print(numeros)