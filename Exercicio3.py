par = 0
impar = 0
cont = 0

while cont < 10:
    cont +=1 
    numero = int(input("Digite um numero: "))
    if numero %2 == 0:
        par += 1
    else:
        impar += 1

    print(f"Quantidade de Pares: {par}")
    print(f"Quantidade de Impares: {impar}")
