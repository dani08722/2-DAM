# Ejercicio 3: Mostrar el precio final (con IVA) de un producto con un valor de 100 euros, suponiendo que el IVA es el 21%.

precio = 100.0
iva = 0.21
precio_final = precio * (1 + iva)

print(f"Precio sin IVA: {precio:.2f} euros")
print(f"IVA (21 %): {precio * iva:.2f} euros")
print(f"Precio final: {precio_final:.2f} euros")