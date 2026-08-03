
def abrir_loja():
    print("=========================")
    print("Bem vindo a Loja ")
    print("Sua Loja favorita")
    print("=========")




def exib_nome(nome,idade):
    print(f"Nome {nome} idade {idade}")



def exibir_etiqueta(nome,preco,categoria):
     print("=====Etiqueta==========")
     print(f"Nome : {nome}")
     print(f"Preço : R$ {preco}")
     print(f"Categoria : {categoria}")
     print("=======================")

produto = {
    "nome":      "Funko Pop Naruto",
    "preco":     79.90,
    "categoria": "Colecionáveis"
}

#exibir_etiqueta(produto["nome"],produto["preco"],produto["categoria"])



def calcular_total(preco, quantidade):
    calculo = preco*quantidade
    return calculo

preco      = 189.90
quantidade = 3
limite     = 500.00


calculado = calcular_total(preco, quantidade)
print(calculado)

if calculado > 500:
    print("Aprove com o gerente")
else:
    print("Aprovado")












