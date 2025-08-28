qtd_Cds = int(input("Quantos CDs voce tem? "))
total = 0.0

for i in range(qtd_Cds):
    valor = float(input("Digite o valor de cada CD: "))
    total += valor

media = total/qtd_Cds
print()


print(f"Voce tem {qtd_Cds} CDs")
print(f"Valor total investido: R$ {total}")
print(f"Valor médio por Cd: R$ {media}")