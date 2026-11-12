# 19. Crear un programa que lea los precios de 5 articulos y las cantidades
# vendidas por una empresa en sus 4 sucursales. Informar de las cantidades
# totales por articulo, las unidades vendidas por sucursal, las recaudaciones
# y la sucursal con mayor recaudacion.

precios = []
ventas = []

# Pedir el precio de cada articulo.
for i in range(5):
    precio = float(input("Introduce el precio del articulo " + str(i + 1) + ": "))
    precios.append(precio)

# Guardar en una lista las ventas de cada sucursal.
# Cada fila contiene las cantidades vendidas de los 5 articulos.
for i in range(4):
    ventasSucursal = []
    print("\nSucursal", i + 1)

    for j in range(5):
        cantidad = int(input("Unidades vendidas del articulo " + str(j + 1) + ": "))
        ventasSucursal.append(cantidad)

    ventas.append(ventasSucursal)

# Calcular las unidades totales que se han vendido de cada articulo.
print("\nUnidades totales vendidas de cada articulo:")
for i in range(5):
    totalArticulo = 0

    for j in range(4):
        totalArticulo = totalArticulo + ventas[j][i]

    print("Articulo", i + 1, ":", totalArticulo)

# Sumar las cantidades de todos los articulos de la sucursal 2.
totalSucursal2 = sum(ventas[1])
print("\nUnidades vendidas en la sucursal 2:", totalSucursal2)

# El articulo 3 esta en la posicion 2 y la sucursal 1 en la posicion 0.
print("Unidades del articulo 3 en la sucursal 1:", ventas[0][2])

# Calcular la recaudacion de cada sucursal.
recaudaciones = []
print("\nRecaudacion de cada sucursal:")

for i in range(4):
    recaudacion = 0

    for j in range(5):
        recaudacion = recaudacion + precios[j] * ventas[i][j]

    recaudaciones.append(recaudacion)
    print("Sucursal", i + 1, ":", round(recaudacion, 2), "euros")

# Calcular la recaudacion total de la empresa.
recaudacionEmpresa = sum(recaudaciones)
print("\nRecaudacion total de la empresa:", round(recaudacionEmpresa, 2), "euros")

# Buscar la sucursal que ha obtenido la mayor recaudacion.
mayorRecaudacion = max(recaudaciones)
sucursalMayorRecaudacion = recaudaciones.index(mayorRecaudacion) + 1
print("La sucursal con mayor recaudacion es la", sucursalMayorRecaudacion)
