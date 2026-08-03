temp_inicial = int(input("Temperatura Inicial "))
temp_final = int(input("Temperatura Final "))



temperatura = temp_inicial
print("=================Escala Termica=================")
print("Temperatura | Barra Visual   | Classificação")
print("----------- | ------------   | -------------")

while temperatura <= temp_final:
    if temperatura <= 0:
        classificacao = "Congelando"
        tamanho_barra = 0 
    elif temperatura <= 5:
        classificacao = "Muito Frio"
        tamanho_barra = 2
    elif temperatura <= 10:
        classificacao = "Frio"
        tamanho_barra = 4
    elif temperatura <= 15:
        classificacao = "Fresco"
        tamanho_barra = 6
    elif temperatura <= 20:
        classificacao = "Agradavel"
        tamanho_barra = 8
    elif temperatura <= 25:
        classificacao = "Quente"
        tamanho_barra = 10
    elif temperatura <= 30:
        classificacao = "Muito Quente"
        tamanho_barra = 12
    else:
        classificacao = "Calor Extremos "
        tamanho_barra = 14
    
    barra = "#"*tamanho_barra

    print(f"  {temperatura:>2}ºC       | {barra:<20} | {classificacao}")

    temperatura = temperatura + 5