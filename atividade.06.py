def selection(lista):
    n = len(lista)
    contador = 0
    for i in range(n):
        #assume que o menor elemento está na posição atual
        posicao_menor = i

        #busca o menor elemento no restante da lista
        for j in range(i+1, n):
            if lista[j] < lista[posicao_menor]:
                posicao_menor = j

    # swap: coloca o menor elemento na posição correta
        lista[i], lista[posicao_menor] = lista[posicao_menor], lista[i]
        contador += 1
    print(lista)
    print(contador)


temperaturas = [38.5,21.3,45.0,30.7,12.9,55.1,9.4]
selection(temperaturas)
