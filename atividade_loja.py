catalogo = [
    {"cod": 1, "produto": "Caneca Star Wars", "valor": 39.90, "qtd_estoque": 25},
    {"cod": 2, "produto": "Camiseta Marvel", "valor": 59.90, "qtd_estoque": 30},
    {"cod": 3, "produto": "Funko Pop Batman", "valor": 89.90, "qtd_estoque": 15},
    {"cod": 4, "produto": "Mousepad Geek RGB", "valor": 49.90, "qtd_estoque": 20},
    {"cod": 5, "produto": "Action Figure Goku", "valor": 129.90, "qtd_estoque": 10},
    {"cod": 6, "produto": "Boné Senhor dos Anéis", "valor": 44.90, "qtd_estoque": 18},
    {"cod": 7, "produto": "Quebra-cabeça Harry Potter", "valor": 69.90, "qtd_estoque": 12},
    {"cod": 8, "produto": "Chaveiro Pokémon", "valor": 19.90, "qtd_estoque": 40},
    {"cod": 9, "produto": "Luminária Mario Bros", "valor": 79.90, "qtd_estoque": 14},
    {"cod": 10, "produto": "Caderno Anime", "valor": 24.90, "qtd_estoque": 35},
]
pedido = []
itens = {}


def busca_produto(codigo):
    for linha in range(len(catalogo)):
        if catalogo[linha]['cod'] == codigo:
           nome_produto = catalogo[linha]['produto']

    return nome_produto 

def verifica_estoque(codigo,quant):
    ver_estoque = False 
    for linha in range(len(catalogo)):
        if catalogo[linha]['cod'] == codigo:
            if quant <= catalogo[linha]['qtd_estoque']:
                ver_estoque = True
            else:
                ver_estoque = False 

def calcula_total(codigo,quant):
    total = 0 
    for linha in range(len(catalogo)):
        if catalogo[linha]['cod'] == codigo:
           total = quant * catalogo[linha]['valor']
           total = round(total,2)
    return total 

continua = False 
while continua == False:
    total_desc = 0
    codigo = int(input("Digite o codigo do Produto: "))
    quant = int(input("Digitr a quantidade desejada: "))
    nome_produto = busca_produto(codigo)
    ver_estoque = verifica_estoque(codigo,quant)
    valor_total = calcula_total(codigo,quant)
    aplicar_desconto =""
    aplicar_desconto = input("Deseja Aplicar desconto S/N: ")
    if aplicar_desconto == "S":
        desconto = int(input("Valor desconto %:  "))
        total_desc = valor_total - ((valor_total*desconto)/100)
        total_desc = round(total_desc,2)
    pergunta_continua = input("Pretende Continuar? S/N")
    itens = {
        "nome": nome_produto,
        "quantidade": quant,
        "Valor_total":valor_total,
        "Valor_Desconto": total_desc
    }
    pedido.append(itens)
    if pergunta_continua == "N":
        continua = True



print("========Relatorio=========")
for linha in pedido:
    print(f"Produto: {linha["nome"]:<13} Qtd {linha["quantidade"]:<13} ")
    print(f"Valor Tot: {linha["Valor_total"]:<13} Valor Desc {linha["Valor_Desconto"]:<13} ")
    print("-----------------------------------")
print("========FIM Relatorio=========")





