# Ejercicio 9: Implementar un programa en Python que pida un número indeterminado de cadenas de caracteres por el teclado, 
# y cuando se finalice dicha introducción, muestre el listado de palabras.



palabras = ""
palabra = input("Introduce una palabra (0 para terminar): ")

while palabra != "0":
    palabras = palabras + palabra + "\n"
    palabra = input("Introduce una palabra (0 para terminar): ")

print("Listado de palabras:")
print(palabras)
