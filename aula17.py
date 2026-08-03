medidas = []

while len(medidas) <= 3:
    peca = float(input(f"peça {(len(medidas)+1)}  "))
    medidas.append(peca)

print(medidas)

aprov =0
reprov =0

for contador in medidas:
    if contador >= 9.8 and contador <= 10.2:
        print(f"{contador} -> Aprovado")
        aprov += 1
    else:
        print(f"{contador} -> Reprovado")
        reprov += 1

print(f"Total Aprovado {aprov}")
print(f"Total Reprovado {reprov}")




lista = ["Kleber","Aluno","Professo"]
lista = "Maçã"

print(lista[1])