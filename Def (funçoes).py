#função
def funcaoSoma(num1, num2):
    soma = num1+num2
    return soma
#programa principal
a = int(input("Digite um numero:"))
b = int(input("Digite mais um numero: "))

soma  = funcaoSoma(a, b)

print(soma)
#função
def funcaoSub(num, num2):
    sub = num - num2
    return sub
#programa principal
a = int(input("Digite um numero: "))
b = int(input("Digite mais um numero: "))

sub = funcaoSub(a,b)

print(sub)

def informação():
    print("Hoje é sexta feira, uhull")
    return 'mas é sexta feira 13'

    
print(informação())