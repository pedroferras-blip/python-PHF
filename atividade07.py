# trabalho sobre conhecimentos em gerais

print ("bem vindo ao quiz sobre conhecimento gerais")
print ("para começar, digite seu nome para salvar e se classificar ")
nome= input("nome:")
resultado=0



print("==============")
print("1-quem ganhou a ultima copa do mundo?")
print("A- Brasil")
print("B- Alemanha")
print("C- Espanha")
print("D- Argentina")
print("se digitar qualquer letra além dessas será automaticamente considerada errada")
resposta=input() # recebe a resposta
resposta= resposta.upper() #deixa tudo em caixa alta para evitar o erro de digitação
resposta= resposta.strip()
if resposta == "D":
    print("sua respota está certa, parabens meu lindo(a)")
    resultado= resultado+1 #se a pessoa acertou ele soma mais um, ou seja é um contador

elif resposta != "D": # o (!= confere se é diferente de tal resposta, por exemplo, diferente de (D))
    print("você errou, que pena")




print("==============")

print("==============")
print("2-qual pesa mais, 1kg de pena ou 1kg de ferro?")
print("A- pena")
print("B- ferro")
print("C- Ambos tem o mesmo peso")
print("D- Pergunta pro tcho lá")
print("se digitar qualquer letra além dessas será automaticamente considerada errada")
resposta=input()
resposta= resposta.upper()
resposta= resposta.strip()

if resposta == "C":
    print("sua respota está certa, parabens meu lindo(a)")
    resultado= resultado+1
elif resposta != "C":
    print("você errou, que pena")





print("==============")

print("==============")
print("3-O brasil tem quantos estados?")
print("A- 20")
print("B- 26+df")
print("C- 27")
print("D- 67")
print("se digitar qualquer letra além dessas será automaticamente considerada errada")
resposta=input()
resposta= resposta.upper()
resposta= resposta.strip()
if resposta == "B":
    print("sua respota está certa, parabens meu lindo(a)")
    resultado= resultado+1
elif resposta != "B":
    print("você errou, que pena")





print("==============")

print("==============")
print("4-Quantos é (50*40)/20?")
print("A- 100")
print("B- 2000")
print("C- 200")
print("D- 102")
print("se digitar qualquer letra além dessas será automaticamente considerada errada")
resposta=input()
resposta= resposta.upper()
resposta= resposta.strip()

if resposta == "A":
    print("sua respota está certa, parabens meu lindo(a)")
    resultado= resultado+1
elif resposta != "A":
    print("você errou, que pena")

print("==============")






print("==============")
print("5-o que é hardware?")
print("A- o sistema")
print("B- não lembro")
print("C- toda a parte fisica(podemos tocar)")
print("D- python")
print("se digitar qualquer letra além dessas será automaticamente considerada errada")
resposta=input()
resposta= resposta.upper()
resposta= resposta.strip()

if resposta == "C":
    print("sua respota está certa, parabens meu lindo(a)")
    resultado= resultado+1
elif resposta != "C":
    print("você errou, que pena")

print("==============")






print("==============")
print("6-Qual os dois principais atores de veloses e furiosos 1?")
print("A- braian e torresmo")
print("B- braian e toretto")
print("C- briano e lucas paqueta")
print("D- casemiro e lula")
print("se digitar qualquer letra além dessas será automaticamente considerada errada")
resposta=input()
resposta= resposta.upper()
resposta= resposta.strip()

if resposta == "B":
    print("sua respota está certa, parabens meu lindo(a)")
    resultado= resultado+1
elif resposta != "B": 
    print("você errou, que pena")




print("==============")
print (f"nome: {nome}")
print(f"o total de acerto foi de: {resultado}")
if resultado >= 5:
    print ("parabéns você acertou todas, foi muito bem")
elif resultado > 3:
    print ("você esta na media, melhore na proxima vez")
elif resultado < 3:
    print("você foi mal, seu conhecimento é baixo")