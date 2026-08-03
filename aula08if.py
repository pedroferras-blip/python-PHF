print("Selecione o modelo do transporte")
print("A - Carro")
print("B - Moto")
print("C - Onibus")
modelo = input("Digite o modelo :") # aqui vai o modelo

if modelo == "A":
    print("Carro")
elif modelo == "C":
    print("Onibus")
elif modelo == "B":
    print("Moto")
else:
    print("Nenhuma modelo")

print("Fim Programa")