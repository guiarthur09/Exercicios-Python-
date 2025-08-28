soma = 0 

while True:
    numero = float(input("Digite um numero : "))

    if numero < 0:
        break
    
    soma += numero

print(f"Soma dos numeros digitados é: {soma}")