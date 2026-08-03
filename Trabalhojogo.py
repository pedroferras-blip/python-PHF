notas = [     #coluna
         [8.5,"Kleber","Professor"], #linha
         [9.8,"Ruam","Aluno"],
         [7.5,"Marcelo","Diretor"]
]

for  l in range(len(notas)):
    for c in range(len(notas[l])):
        print(notas[l][c])
