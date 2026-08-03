pedidos = [
    ["Pizza",        "Lanche",    45.90],
    ["Acai",         "Sobremesa", 32.00],
    ["X-Burguer",    "Lanche",    28.50],
    ["Frango Frito", "Prato",     38.90]
]


total = 0
for i in range(len(pedidos)):
    print(f"Produto:{pedidos[i][0]}   Categoria:{pedidos[i][1]}   Preço: {pedidos[i][2]} ")
    if pedidos[i][1] == "Lanche":
        total += pedidos[i][2]

print("_______________________________")
print(f"Total gasto com Lanche {total}")
