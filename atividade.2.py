
def maior_numero(lista, i = 0):

    o = 0
    if i <= len(lista)  :
        return lista
    maior = lista[i]
    menor = lista[o+1]
    maior_numero(lista,i + 1 )
    if maior >= menor:
        maior = menor
    lista.remove(maior) 
    return maior



lista = [18, 55, 7, 42, 91, 26, 63]

maior = maior_numero(lista)
print(maior)
