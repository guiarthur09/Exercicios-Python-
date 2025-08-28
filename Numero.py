def inteiro_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero **0.5) + 1):
        if numero %2 == 0:
            return False
        return True
    
n = int(input("Digite um valor positivo: "))

print(f"Números primos de 1 até {n}: ")
for i in range(1, n, +1):
    if inteiro_primo(i):
        print(i, end=" \n")