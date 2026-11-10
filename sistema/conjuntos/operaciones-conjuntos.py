# En los conjuntos no se accede a elementos por posicion ni se modifican
# elementos concretos, porque no tienen un orden establecido.

# add() anade un elemento. Si ya existe, el conjunto sigue teniendo una copia.
beatles = {"Lennon", "McCartney", "Harrison", "Starr"}
beatles.add("Best")
print(beatles)

# remove() borra el elemento indicado. Da error si no se encuentra.
beatles.remove("Best")
print(beatles)

# len() devuelve el numero de elementos (cardinalidad).
print(len(beatles))

# Se puede recorrer un conjunto con un bucle for.
for integrante in beatles:
    print(integrante)

# in comprueba si un elemento pertenece al conjunto.
print("Lennon" in beatles)
print("Best" in beatles)

# sorted() devuelve una lista nueva con los elementos ordenados.
# No ordena el conjunto original ni existe el metodo sort() para set.
calificaciones = {8, 4, 6, 2, 9, 5}
print(sorted(calificaciones))
