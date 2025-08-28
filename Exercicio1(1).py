num = int(input("Digite o Primeiro Número: "))
num2 = int(input("Digite o Segundo Número: "))

if num <= num2:
   for i in range(num, num2 + 1):
    print(i)
else:
    for j in range(num, num2 - 1, -1):
        print(j)