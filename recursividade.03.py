def somar(lista, i=0):
    if i == len(lista):
        return 0
    meu_numero = lista[i]
    resposta_do_proximo = somar(lista, i + 1)
    resultado = meu_numero + resposta_do_proximo
    return resultado

numeros=[10,20, 30, 40, 50]
print(f"soma: {somar(numeros)}")