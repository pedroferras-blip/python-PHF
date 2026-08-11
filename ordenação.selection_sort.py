def selection(lista):
    n = len(lista)

    for i in range(n):
        #assume que o menor elemento está na posição atual
        posicao_menor = i

        #busca o menor elemento no restante da lista
        for j in range(i+1, n):
            if lista[j] < lista[posicao_menor]:
                posicao_menor = j

    # swap: coloca o menor elemento na posição correta
        lista[i], lista[posicao_menor] = lista[posicao_menor], lista[i]

    return lista

#exeplo de usa 

lista = [5,3,8,1]

resul =selection(lista)
print(resul)