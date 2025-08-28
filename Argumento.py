def verificar_num(numero):
    if numero > 0:
        return 'P'
    else:
        return 'N'

numero = int(input("Digite um Numero: "))
resultado = verificar_num(numero)
print(f"Resultado: {resultado}")