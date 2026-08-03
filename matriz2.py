loja = [
    ["tv",         "samsung",   4800,"eletrônicos"],
    ["geladeira",  "brastemp",  3200,"eletrodomésticos"],
    ["micro-ondas","electrolux", 950,"eletrodomésticos"],
    ["tablet",     "LG",         1800,"eletronicos"]
]
soma = 0
for linha in range(len(loja)):
    if loja[linha][2] >= 1000:
        print(f"Produto {loja[linha][0]} valor R$ {loja[linha][2]}")
        soma += loja[linha][2]

print(f"Total {soma}")


    