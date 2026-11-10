# Las claves de un diccionario deben ser hashables: su hash debe mantenerse
# estable mientras se usan como clave. Por eso se usan objetos inmutables.

diccionario = {
    10: "entero",
    3.14: "decimal",
    "hola": "cadena",
    ("a", "b"): "tupla",
}
print(diccionario)

# hash() permite consultar el hash de un objeto hashable.
print(hash("hola"))
print(hash(("a", "b")))

# Una lista es mutable y no se puede usar como clave:
# hash(["a", "b"])  # TypeError: unhashable type: 'list'
