#atividade
def tabuada(n,n2):
    if n2 == 11:
        print("fim" )        
        return 0
    resultado = n * n2
    tabuada(n ,n2 + 1)
    print(f"{n} X {n2} = {resultado}")
    return resultado


tabuada(int(input("digite a tabuada que você quer: ")),int(input("digite aode você quer começar: ")))
    

    


