def bubble_sort(lista):
    n = len(lista)

    for i in range(n):

        # a cada passagem,o maior elemento vai para o final

        for j in range(0,n-1):

            #compara elemento vizinhos

            if lista[j] > lista[j+1]:

            # swap : troca os elemento de posição
            
                lista[j], lista[j+1] = lista[j+1],lista[j]


    return lista



array = [5,3,8,1]

resultado = bubble_sort(array)

print(resultado)