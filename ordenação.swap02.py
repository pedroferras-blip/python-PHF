jogadores =[
    {"nome": "ana","pontos": 74},
    {"nome": "carlos","pontos": 95},
    {"nome": "beatriz","pontos": 65}
]

def ordenar_pontos(lista):
    n = len(lista)

    for linha in range(n):
        for j in range(n-1):
           if jogadores[j]["pontos"] < jogadores[j+1]["pontos"] :
               jogadores[j],jogadores[j+1] = jogadores[j+1],jogadores[j]  

    return jogadores



resul=ordenar_pontos(jogadores)
print(resul)