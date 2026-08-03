notas = []   # lista vazia

while len(notas) < 4:
    nota = float(input(f"Nota {len(notas)+1}: "))
    notas.append(nota)

print(f"Notas registradas: {notas}")

for contador in notas:    
    if contador >= 7.5 and contador < 8.9:
        print(f"{contador} -> Aprovado")
    else:
        print(f"{contador} -> Reprovado")
   


