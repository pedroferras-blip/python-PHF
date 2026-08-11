produtos = [
    {"nome": "Teclado",  "quantidade": 15, "preco": 120.00},
    {"nome": "Monitor",  "quantidade":  8, "preco": 850.00},
    {"nome": "Mouse",    "quantidade": 30, "preco":  75.00},
    {"nome": "Headset",  "quantidade": 12, "preco": 200.00},
    {"nome": "Webcam",   "quantidade":  5, "preco": 310.00},
]


n = len(produtos)


for i in range(n):

    posicao_menor = i

    for j in range(i+1, n):
            if produtos[j]["preco"] < produtos[posicao_menor]["preco"]:
                posicao_menor = j

    produtos[i], produtos[posicao_menor] = produtos[posicao_menor], produtos[i]


for i in range(n):
     print(f"{i+1}º - `{produtos[i]['nome']}  | Qtd {produtos[i]['quantidade']}  | preço R$ {produtos[i]['preco']}")