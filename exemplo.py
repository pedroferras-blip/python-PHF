produto = {
    "nome":     "Controle PS5 DualSense",
    "preco":    499.90,
    "estoque":  5,
    "parcelas": 10,
    "marca": "Sony"
}

for linha in produto:    
    if type(produto[linha]) == str:
        print(f"{linha}: {produto[linha]}")
    if type(produto[linha]) == float:
        print(f"{linha}: R$ {produto[linha]}")
    if type(produto[linha]) == int:
        print(f"{linha}: {produto[linha]}")

print("==============================")
tot_est = produto["preco"]*produto["estoque"]
print(f"Total em estoque R$ {tot_est} ")
tot_parc = produto["preco"]/produto["parcelas"]
print(f"Valor das parcelas {round(tot_parc,2)} ")