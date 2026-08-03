produto = input("Informe o Produto")
preco = float(input("Preço do Produto "))
quantidade = float(input("Quantidade "))
desconto = float(input("Desconto"))
subtotal = quantidade * preco
total_geral = subtotal - desconto

print("==========Cupom Fiscal=============")
print(f"Produto: {produto}")
print(f"Quantidade: {preco}")
print(f"Preço Uni: {quantidade}")
print(f"Subtotal: {(quantidade * preco)}")
print(f"Desconto: {desconto}")
print(f"Total Geral: {(subtotal - desconto)}")
print("--------------------------------")