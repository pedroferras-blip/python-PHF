numeros = [42,-7,15,8,-3,73,27,-1,56,19]
def orde(lista):
    contador = 0
    for i in range(len(lista)):

        for j in range(len(lista)-1):
            if  lista[j]  > 0 :
                if lista[j] > lista[j+1]:        
                    lista[j],lista[j+1] =lista[j+1],lista[j]
                    contador += 1

    print(lista)
    print(contador)
    
orde(numeros)

