# Los diccionarios tambien se pueden construir por comprension.
# La forma es {clave: valor for elemento in iterable}.
palabras = ("sol", "espacio", "cohete", "tierra")
longitud_palabras = {palabra: len(palabra) for palabra in palabras}
print(longitud_palabras)

# Se puede anadir una condicion al final de la comprension.
# Aqui solo guardamos palabras que no empiezan por vocal.
palabras_sin_vocal_inicial = {
    palabra: len(palabra)
    for palabra in palabras
    if palabra[0] not in "aeiou"
}
print(palabras_sin_vocal_inicial)
