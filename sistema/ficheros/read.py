# Con read
f = open("ficheros/files/prueba.txt", "r")

print(f.read())
print("--------------------------------------------------------\n\n\n\n\n")

# Si ya lo hemos iterado y lo volvemos a leer no lee nada
print(f.readlines())
print("--------------------------------------------------------\n\n\n\n\n")

# Readlines
f = open("ficheros/files/prueba.txt", "r")
print(f.readlines())
print("--------------------------------------------------------\n\n\n\n\n")

# Linea por linea
f = open("ficheros/files/prueba.txt", "r")

for line in f:
    print(line.strip())