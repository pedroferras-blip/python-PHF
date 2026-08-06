def calcule_tabu(n):
     if n == 0:
            print("fim" )
            return 
     camada= "camada"+str(n)
     total= 5*n
     resultado = "5x"+str(n)+"="+str(total)
     calcule_tabu(n-1)
     print(camada)
     print(resultado)

calcule_tabu(int(input("digite um numero")))
    