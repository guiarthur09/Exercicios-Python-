vetor = [0] * 6
a = 0

for i in range(len(vetor)):
    vetor[i] = i
print(vetor[1:3])

notas = []

n = int(input("Entre com o numeros de notas: "))
for i in range(n):
    dados = float(input("Entre com a nota " + str(i) + ": "))
    notas.append(dados)
print(notas)


