import random

numero_secreto = random.randint(1, 20)
tentativas = 0

while True:
    n = int(input("Digite um Número: "))
    tentativas+=1
    if n == numero_secreto:
        print(f"Acertou! O número secreto era {numero_secreto}")
        print(f"Voce acertou em {tentativas} tentativas.")
        break
    if n != numero_secreto:
        print("Errou! Tente Novamente")

