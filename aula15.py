materiais = ["Lapis","Caneta","Caderno","Livro"]
print("Primeira Lista")
print(materiais)
print("********************")
#############################################
materiais.append("Apagador")
materiais.append("Canetão")
print("Lista Com Append")
print(materiais)
print("********************")
##############################################
materiais.remove("Caneta")
print("Lista com remove")
print(materiais)
print("********************")
##############################################

print(f" Tota de  Itens {len(materiais)}")

for contador in materiais:
    print(f" - {contador}")

