vendas = [
    {"nome": "Funko Pop Naruto", "preco": 79.90, "qtd": 5, "desc": 10},
    {"nome": "HQ Batman: Ano Um", "preco": 59.90, "qtd": 3, "desc": 0},
    {"nome": "Camiseta The Witcher", "preco": 89.90, "qtd": 4, "desc": 20},
]

def calcular_fatur(prv1,qtd1,desc1):
    total = prv1*qtd1
    total_desc = total - (total*desc1/100)
    return total_desc

print("=========Relatorio==================")
total_fat = 0
for i in range(len(vendas)):
    prv = vendas[i]["preco"]
    qtd = vendas[i]["qtd"]
    desc = vendas[i]["desc"]
    valor_total =calcular_fatur(prv,qtd,desc)
    print(f"{vendas[i]["nome"]} R$ {valor_total}")
    total_fat += valor_total
print("===========================")
print(f"Total Faturado R$ {round(total_fat,2)}")