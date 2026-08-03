#Conversão de Tipo de Variavel
numero_texto = "42" #iniciado como str
numero_inteiro = int(numero_texto) # converte para numero inteiro
numero_real = float(numero_texto) # converte para numero descimal

valor = 19.256
valor_texto = str(valor)
valor_inteiro = int(valor)
print(numero_texto)
print(valor)

vazio = None

#Se Nada/Zero ou vazio é Falso
print(bool(0)) #False 
print(bool("")) #False
print(bool("Texto")) #True
print(bool(1)) #True
print(bool(vazio)) #Fase