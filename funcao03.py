
def fun_soma(A,B):
    resultado = A+B
    return resultado
   

def fun_sub(A,B):
    resultado = A-B
    return resultado

def verifica_diferente(A,B):
    validador = False
    if A != B :
        validador = True        
    else:
        validador = False
       
    return validador  
    
    
dado1 = input("Digite palavra 1")
dado2 = input("Digite palavra 2")

confere = verifica_diferente(dado1,dado2)

if confere == True:
    print("Diferente")
else:
    print("Igual")


