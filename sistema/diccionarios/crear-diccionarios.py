# Un diccionario guarda pares de clave: valor.
# Las claves son unicas y el diccionario conserva el orden de insercion.
# Es mutable: se pueden anadir, modificar y borrar elementos.

# Diccionario vacio: {}. dict() tambien permite crear uno vacio.
diccionario_vacio = {}

# Las claves pueden ser de distintos tipos inmutables.
rae = {
    "bifronte": "De dos frentes o dos caras",
    "anarcoide": "Que tiende al desorden",
    "montuvio": "Campesino de la costa",
}

poblacion = {
    2015: 2_135_209,
    2016: 2_154_924,
    2017: 2_177_048,
}

print(diccionario_vacio)
print(rae)
print(poblacion)

# No hay que llamar dict a una variable, porque ocultaria la funcion dict().
