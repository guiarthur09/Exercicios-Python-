soma_idades = 0
qtd_regular = 0
qtd_bom = 0
qtd_execelente = 0

def coletar_idade():
    idade = int(input("Informe a sua Idade: "))
    return idade

def coletar_opiniao():
    print("Opinião sobre a estreia do Filme Coringa:")
    print("1) Regular")
    print("2) Bom")
    print("3) Execelente")
    print()
    opiniao = int(input("Sua Opinião: "))
    return opiniao

for i in range(20):
    idade = coletar_idade()
    opiniao = coletar_opiniao()

    soma_idades += idade

    if opiniao == 1:
        qtd_regular+=1
    if opiniao == 2:
        qtd_bom+=1
    if opiniao == 3:
        qtd_execelente+=1

media_idades = soma_idades / 20

print("\nResultado da Pesquisa: ")
print(f"Média de Idades: {media_idades:.0f} anos")
print(f"Quantidade de pessoas que responderam 'Execelente': {qtd_execelente}")
print(f"Quantidade de pessoas que responderam 'Bom': {qtd_bom}")
print(f"Quantidade de pessoas que responderam 'Regular': {qtd_regular}")




    