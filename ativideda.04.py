alunos = [
    {"nome": "Lucas",    "idade": 20, "media": 7.5, "faltas": 3},
    {"nome": "Fernanda", "idade": 22, "media": 9.2, "faltas": 1},
    {"nome": "Rafael",   "idade": 21, "media": 6.8, "faltas": 5},
    {"nome": "Juliana",  "idade": 19, "media": 8.1, "faltas": 2},
]


def ordenar_pontos(lista):
    n = len(lista)

    for linha in range(n):
        for j in range(n-1):
           if alunos[j]["media"] < alunos[j+1]["media"] :
               alunos[j],alunos[j+1] = alunos[j+1],alunos[j]  

    return alunos



resul = ordenar_pontos(alunos)

print(resul)