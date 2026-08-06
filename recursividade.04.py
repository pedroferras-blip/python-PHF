total = 0 
def somar(lista,i=0):
   
    if i == len(lista):
        return 
    valor = lista[i]
    somar(lista,i+1)
    global total
    print(valor)

    total = total+valor
    





numeros=[10,20,30,40,50]
somar(numeros)

