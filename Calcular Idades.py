def classificar_Idade(idade):
    if idade < 12:
        return 'Criança'
    elif idade >= 12 and idade <= 17:
        return 'Adolescente'
    elif idade >= 18:
        return 'Adulto'
    else:
        return 'Idade Invalida'
    
idade = int(input("Digite a sua Idade: "))
idade = classificar_Idade(idade)
print(f"Classificação : {idade}")
    

    