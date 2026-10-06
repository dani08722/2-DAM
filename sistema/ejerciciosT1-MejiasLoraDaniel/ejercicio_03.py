# Ejercicio 3: calcular el precio final de un producto con IVA del 21 %.

precio = 100.0
iva = 0.21
precio_final = precio * (1 + iva)

print(f"Precio sin IVA: {precio:.2f} euros")
print(f"IVA (21 %): {precio * iva:.2f} euros")
print(f"Precio final: {precio_final:.2f} euros")