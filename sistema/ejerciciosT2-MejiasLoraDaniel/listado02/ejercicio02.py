productos = ("pan", "leche", "huevos", "queso")

print(productos)


print(productos[0],productos[-1])


producto_elegido= "leche"
cantidad = productos.count(producto_elegido)
# Mostramos el resultado
print(f"El producto '{producto_elegido}' aparece {cantidad} vez.")


listaProductos=list(productos)
listaProductos[1]="cereal"
print(listaProductos)
productos=tuple(listaProductos)
print(productos)


productos = productos + ("café",)
print(productos)