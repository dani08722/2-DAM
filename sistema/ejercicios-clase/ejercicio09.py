palabras = []
palabra = input("Introduce una palabra (Enter para terminar): ")

while palabra != "":
    palabras.append(palabra)
    palabra = input("Introduce otra palabra (Enter para terminar): ")

print("Palabras introducidas:", palabras)