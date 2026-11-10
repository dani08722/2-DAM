# Las tuplas son inmutables: no se pueden modificar despues de crearlas.
# Por eso no tienen los metodos de modificacion de las listas.

frutas = ("manzana", "pera", "naranja")
print("Tupla original:", frutas)

# reverse() modifica una lista "in-situ" y no se puede usar con tuplas.
# reversed() si acepta tuplas: devuelve un iterador, sin cambiar la original.
al_reves = tuple(reversed(frutas))
print("Al reves:", al_reves)

# append() agrega un elemento al final de una lista.
# Para crear una tupla nueva, se concatena con otra tupla.
frutas_con_otra = frutas + ("uva",)
print("Agregar un elemento:", frutas_con_otra)

# extend() agrega varios elementos a una lista.
# En una tupla se pueden concatenar varias tuplas.
mas_frutas = frutas + ("uva", "kiwi")
print("Agregar varios elementos:", mas_frutas)

# remove() elimina de una lista la primera coincidencia.
# En una tupla se puede crear otra tupla sin ese elemento.
sin_pera = tuple(fruta for fruta in frutas if fruta != "pera")
print("Sin pera:", sin_pera)

# clear() vacia una lista.
# Para obtener una tupla vacia, se crea una nueva con ().
vacia = ()
print("Tupla vacia:", vacia)

# sort() ordena una lista "in-situ" y no se puede usar con tuplas.
# sorted() si acepta tuplas, pero devuelve una lista nueva.
# tuple() permite convertir ese resultado de nuevo en una tupla.
ordenadas = tuple(sorted(frutas))
print("Ordenadas:", ordenadas)

# Resumen:
# reverse(), append(), extend(), remove(), clear() y sort() son metodos
# de listas, no de tuplas. Para cambiar datos, se crea una tupla nueva.
