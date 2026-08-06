def ordenar_maior_para_menor(lista):
    if len(lista) <= 1:              # caso base
        return lista

    maior = max(lista)               # encontra o maior valor da lista atual
    lista.remove(maior)              # remove esse valor da lista para não repeti-lo

    return [maior] + ordenar_maior_para_menor(lista)   # chamada recursiva
#A cada chamada recursiva uma lista parcial é criada
# em memória e concatenada com o resultado da próxima chamada.


precos = [89.90, 45.00, 120.00, 33.50, 210.00, 67.80]

ordenado = ordenar_maior_para_menor(precos)

print("Lista original:")
for preco in precos:
    print(f"  R$ {preco:.2f}")

print("\nLista ordenada (maior para menor):")
for preco in ordenado:
    print(f"  R$ {preco:.2f}")