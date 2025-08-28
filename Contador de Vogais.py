vogais = ['a', 'e', 'i', 'o', 'u']
cont = 0

frase = input("Digie um Frase: ").lower()

for letra in frase:
    if letra in vogais:
        cont +=1

print(f"Quantidade de Vogais: {cont}")