senha = "" 
tentativas = 0 
while tentativas < 3: 
    senha = input("Digite a senha: ") 
    if senha == "1234": 
        print("Acesso concedido!") 
    tentativas = tentativas + 1 