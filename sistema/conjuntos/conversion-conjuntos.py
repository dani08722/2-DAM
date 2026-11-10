# set() convierte cualquier iterable en un conjunto.
# Los elementos repetidos se guardan una sola vez.

letras = set("platanada")
print(letras)

numeros = set([1, 2, 2, 3, 3, 3, 4, 4, 5])
print(numeros)

# Al pasar un diccionario, se obtienen sus claves.
colores_frutas = {"manzana": "rojo", "platano": "amarillo", "kiwi": "verde"}
frutas = set(colores_frutas)
print(frutas)

# El orden mostrado puede cambiar: no se debe confiar en el orden de un set.
