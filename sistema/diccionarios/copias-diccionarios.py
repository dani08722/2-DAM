# La asignacion no crea una copia: ambas variables apuntan al mismo diccionario.
diccionario_original = {"a": 1, "b": 2}
referencia = diccionario_original
diccionario_original["a"] = 99
print(referencia)  # Tambien refleja el cambio.

# copy() crea una copia superficial independiente del diccionario original.
diccionario_original = {"a": 1, "b": 2}
copia = diccionario_original.copy()
diccionario_original["a"] = 50
print(diccionario_original)
print(copia)

# Si hay listas u otros objetos mutables dentro, copy() no copia esos objetos.
# Para copiar tambien los elementos internos se puede usar deepcopy().
from copy import deepcopy

original_con_lista = {"notas": [7, 8]}
copia_profunda = deepcopy(original_con_lista)
original_con_lista["notas"].append(10)
print(original_con_lista)
print(copia_profunda)
