num = int(input("Digite o Primeiro Número: "))
num2 = int(input("Digite o Segundo Número: "))

soma = 0

if num <= num2:
   for i in range(num, num2 + 1):
    print(i)
    soma +=i
else:
    for j in range(num, num2 - 1, -1):
        print(j)
        soma += j

print()
print(f"A soma dos numeros de {num} a {num2} é: {soma}")
