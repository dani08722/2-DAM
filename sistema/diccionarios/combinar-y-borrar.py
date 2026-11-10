# Al combinar diccionarios, las claves nuevas se incorporan.
# Si se repite una clave, prevalece el valor del diccionario de la derecha.
diccionario_1 = {"a": 1, "b": 2}
diccionario_2 = {"b": 20, "c": 3}

# ** crea un diccionario combinado sin modificar los originales.
combinado = {**diccionario_1, **diccionario_2}
print(combinado)

# Desde Python 3.9 tambien se puede usar | para combinar.
print(diccionario_1 | diccionario_2)

# update() incorpora los pares al diccionario original y lo modifica.
diccionario_1.update(diccionario_2)
print(diccionario_1)

# del borra un elemento por su clave.
del diccionario_1["a"]
print(diccionario_1)

# pop() borra la clave y devuelve su valor.
valor_borrado = diccionario_1.pop("b")
print(valor_borrado)
print(diccionario_1)

# clear() vacia el mismo diccionario.
diccionario_1.clear()
print(diccionario_1)

# Tambien se puede asignar {} para que la variable apunte a uno vacio.
diccionario_1 = {"x": 10}
diccionario_1 = {}
print(diccionario_1)
