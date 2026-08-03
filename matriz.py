produto = [
    ["Coca-Cola","Refri", 12.50, 25],
    ["Bolacha",  "Comida", 3.50, 30],
    ["Alcatra",  "Carne", 39.90, 120]
]
soma = 0
controle = 0
for linha in range(len(produto)):# Cria range, calcula linhas matriz
    if (produto[linha][2]) >= 10:#Compara apenas valor maior a 10
      controle = (produto[linha][2]*produto[linha][3]) #Soma tot cad prod
      print(f"Soma total prod {linha+1} é igual a {controle}") 
      soma += (produto[linha][2]*produto[linha][3]) # Acumulado da soma
      
print(f"O Valor Total em Estoque R$ {soma}")


  