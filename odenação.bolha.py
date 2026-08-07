lista = [5,3,1,4,2]

for i in range(len(lista)):
    for j in range(len(lista)-1):
        if lista[j] > lista[j+1]:
            lista[j],lista[j+1] =lista[j+1],lista[j]

print(lista)