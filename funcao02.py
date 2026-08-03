def calculo_total(valor,desconto,quant):
    total = valor*quant
    tot_desc = total - (total*desconto/100)
    return tot_desc

produto = "Computador"
valor = 1500
desconto = 20
quant_vendida = 5

valor_tot_desc= calculo_total(valor,desconto,quant_vendida)

print(f"Produto {produto} total vendido {quant_vendida} valor total com desconto {valor_tot_desc}")


