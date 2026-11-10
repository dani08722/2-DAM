# Creamos una tupla con tres nombres.
three_wise_men = ("Melchor", "Gaspar", "Baltasar")

# Guardamos cada nombre en una variable.
king1, king2, king3 = three_wise_men

# Mostramos cada nombre.
print(king1)
print(king2)
print(king3)


print("----------------------------------------------------------------------")


# divmod devuelve el cociente y el resto.
quotient, remainder = divmod(7, 3)

# Mostramos el cociente y el resto.
print(quotient)
print(remainder)


print("----------------------------------------------------------------------")


# Intercambiamos los valores de las variables.
value1 = 40
value2 = 20
value1, value2 = value2, value1

# Mostramos los valores intercambiados.
print(value1)
print(value2)


print("----------------------------------------------------------------------")


# El * recoge los elementos intermedios en una lista.
ranking = ("G", "A", "R", "Y", "W")
head, *body, tail = ranking

# Mostramos el primero, los del medio y el ultimo.
print(head)
print(body)
print(tail)


print("----------------------------------------------------------------------")


# Las cadenas tambien se pueden desempaquetar.
oxygen = "O2"
first, last = oxygen
print(first, last)

# El * recoge los caracteres del medio en una lista.
text = "Hello, World!"
head, *body, tail = text
print(head, body, tail)

# Tambien podemos desempaquetar una lista.
writer1, writer2, writer3 = ["Virginia Woolf", "Jane Austen", "Mary Shelley"]
print(writer1, writer2, writer3)

# split() crea una lista con las palabras.
text = "Hello, World!"
word1, word2 = text.split()
print(word1, word2)


print("----------------------------------------------------------------------")


# Los parentesis crean un generador, no una tupla.
myrange = (number for number in range(1, 6))
print(type(myrange))

# tuple() convierte los valores en una tupla.
mytuple = tuple(number for number in range(1, 6))
print(mytuple)




