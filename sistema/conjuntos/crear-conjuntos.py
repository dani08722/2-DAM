# Un conjunto (set) guarda valores unicos y no mantiene un orden fijo.
# Sus elementos deben ser hashables, por ejemplo numeros o cadenas.

numeros_loteria = {21, 10, 46, 29, 31, 94}
print(numeros_loteria)

# Para crear un conjunto vacio hay que usar set().
# Las llaves vacias {} crean un diccionario, no un conjunto.
conjunto_vacio = set()
print(conjunto_vacio)
print(type(conjunto_vacio))

# No se debe asignar el nombre set a una variable, porque ocultaria la funcion.
