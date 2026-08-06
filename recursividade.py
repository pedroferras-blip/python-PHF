def contador(n):
    if n == -25:
        print("fim" )
        return 
    print("faz o l")
    contador(n-5)


contador(5)

def soma(n):
    if n == 0:
        return 
    return n + soma(n-1)

resul = soma(10)

print(resul)