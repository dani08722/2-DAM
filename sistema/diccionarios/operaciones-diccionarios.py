# Se accede a un valor usando su clave entre corchetes.
rae = {
    "bifronte": "De dos frentes o dos caras",
    "anarcoide": "Que tiende al desorden",
    "montuvio": "Campesino de la costa",
}

print(rae["anarcoide"])

# Si la clave no existe, los corchetes producen KeyError.
# get() devuelve None si no encuentra la clave, o un valor alternativo indicado.
print(rae.get("programacion"))
print(rae.get("programacion", "No disponible"))

# Asignar a una clave existente cambia su valor.
# Asignar a una clave nueva agrega un par clave-valor.
rae["enjuiciar"] = "Someter una cuestion a examen y juicio"
rae["enjuiciar"] = "Instruir, juzgar o sentenciar una causa"
print(rae)

# in comprueba si una clave esta en el diccionario.
print("bifronte" in rae)
print("almohada" not in rae)

# keys(), values() e items() permiten consultar claves, valores y pares.
print(rae.keys())
print(rae.values())
print(rae.items())

# len() cuenta los pares clave-valor.
print(len(rae))

# Se puede iterar sobre claves, valores o pares.
for palabra in rae.keys():
    print(palabra)

for significado in rae.values():
    print(significado)

for palabra, significado in rae.items():
    print(f"{palabra}: {significado}")
