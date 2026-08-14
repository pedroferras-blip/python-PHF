
def maior_numero(lista, i = 0):
    if i >= len(lista):
        return i

    for maior in lista:
        if maior >  i:

            menor = maior
            i = menor
   

    return maior_numero(lista, i)



def maior_numero1(lista, i = 0,maior = 0):
    if i >= len(lista):
        return maior

    numero_atual = lista[i]

    if numero_atual > maior:
        maior = numero_atual

    resposta = maior_numero1(lista, i + 1,maior)

    return resposta
      

lista = [18, 55, 7, 42, 91, 26, 63]

maior = maior_numero(lista)
maior1 = maior_numero1(lista)
print(f"maior número é: {maior}")
print(f"maior número é: {maior1}")