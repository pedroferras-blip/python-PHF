valor_total_compra = float(input("Valor total da compra "))
qts_parcelas = int(input("Total de Parcelas "))
contador = 1
total_pago = 0
saldo_dev = 0
valor_parcela = valor_total_compra/qts_parcelas

print(valor_parcela)

while contador <= qts_parcelas:
    total_pago = total_pago + valor_parcela
    saldo_dev = valor_total_compra - total_pago
    print(f"{contador} | {valor_parcela} | {total_pago}  | {saldo_dev}")
    contador = contador+1
