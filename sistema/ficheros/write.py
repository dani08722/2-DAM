# 1. Escribir (crea el fichero o lo sobrescribe si ya existe)
f = open("ejemplo.txt", "w")
f.write("Primera línea\n")
f.write("Segunda línea\n")

# 2. Añadir al final sin borrar lo anterior
f=open("ejemplo.txt", "a")
f.write("Tercera línea (añadida)\n")

# 3. Escribir varias líneas de golpe con writelines
lineas = ["Línea A\n", "Línea B\n", "Línea C\n"]
f = open("lista.txt", "w")
f.writelines(lineas)

f = open("lista.txt", "r")
print(f.read())
print("--------------------------------------------------------\n\n\n\n\n")

# 4. Leer para comprobar el resultado
f = open("ejemplo.txt", "r")
print(f.read())
