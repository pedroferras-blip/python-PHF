selecao = {
    "nome":     "Brasil",
    "jogos":    7,
    "gols":     17,
    "vitorias": 6,
    "grupo":    "C"
}
#[ÓTIMA CAMPANHA]
mensagem = ""
print("=======Ficha Seleção===========")
for linnha in selecao:
    if linnha == "vitorias":
        if selecao[linnha] > 5:
            mensagem = "[ÓTIMA CAMPANHA]"

    print(f"{linnha} : {selecao[linnha]} {mensagem} ")
    mensagem = ""

print("=======================")
media = (selecao["gols"]/selecao["jogos"])
print(f"Media de Gols {round(media,2)} ")
#(vitorias / jogos) * 100;
aproveitamento = ((selecao["vitorias"]/selecao["jogos"])*100)
print(f"Aproveitamento {round(aproveitamento,2)} %")
