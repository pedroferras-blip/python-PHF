selecoes = [
    {"nome": "Brasil",   "gols_pro": 12, "gols_contra": 4, "vitorias": 4},
    {"nome": "França",   "gols_pro": 9,  "gols_contra": 5, "vitorias": 3},
    {"nome": "Marrocos", "gols_pro": 6,  "gols_contra": 7, "vitorias": 2},
    {"nome": "Croácia",  "gols_pro": 8,  "gols_contra": 6, "vitorias": 3},
]

saldo = 0
saldo_total = 0 
for linha in selecoes:
    classificado = ''    
    saldo = ((linha['gols_pro'])-linha['gols_contra'])
    saldo_total += saldo
    if linha['vitorias'] >= 3:
        classificado = "[CLASSIFICADO]"
    else:
        classificado = "[NÃO CLASSIFICADO]"

    print(f"{linha['nome']:<9} | Pró {linha['gols_pro']:<9} | "
          f"Contra {linha['gols_contra']:<9} | Saldo {saldo:<9} | Vitorias {linha['vitorias']}  | {classificado}")
    

print("=======================================")
print(f"Saldo Total de Gols {saldo_total}")