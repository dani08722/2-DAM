# frozenset() crea un conjunto inmutable a partir de cualquier iterable.
# Inmutable significa que no podemos anadir ni borrar elementos despues de crearlo.

calificaciones = [1, 3, 2, 3, 1, 4, 2, 4, 5, 2, 5, 5, 3, 1, 4]
niveles_calificaciones = frozenset(calificaciones)

print(niveles_calificaciones)
# Se eliminan los valores repetidos, igual que al crear un set normal.

# Los conjuntos inmutables no tienen metodos de modificacion como add().
# Si intentamos ejecutar esta linea, Python produce un AttributeError:
# niveles_calificaciones.add(50)
