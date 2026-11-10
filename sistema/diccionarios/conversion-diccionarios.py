# dict() convierte en diccionario un iterable formado por pares de elementos.

desde_cadenas = dict(["a1", "b2"])
print(desde_cadenas)

desde_tuplas = dict((("a", 1), ("b", 2)))
print(desde_tuplas)

# Tambien se puede crear pasando argumentos con nombre.
# En este caso, los nombres deben ser identificadores validos de Python.
persona = dict(nombre="Guido", apellido="Van Rossum", trabajo="Creador de Python")
print(persona)

# fromkeys() crea claves con un mismo valor inicial.
vocales = dict.fromkeys("aeiou", 0)
print(vocales)

# dict() sin argumentos crea un diccionario vacio.
print(dict())
