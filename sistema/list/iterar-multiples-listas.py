shopping = ["Agua❘", "Aceite", "Arroz"]

details = ["mineral natural", "de oliva virgen", "basmati"]

for product, detail in zip(shopping,details):
    print(product, detail)

todo=list(zip(shopping,details))
print(todo)

