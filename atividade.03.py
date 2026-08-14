def reversão(lista):
    if len(lista) <= 1:              
        return lista

    maior = max(lista)            
    lista.remove(maior)             
    return [maior] + reversão(lista) 


lista = [10, 25, 38, 47,52, 61, 79, 84]

numero=reversão(lista)
print(numero)