import time 

saldo_atual = 1000

def identificação():
    print("...")
    time.sleep(2)
    print("\nBEM VINDO AO CAIXA DO BRASIL\n")
    time.sleep(1)
    nome = input("Digite seu Nome: ")
    time.sleep(1)
    senha = input("Digite a sua Senha: ")
    while senha != "123":
        print("\n...")
        time.sleep(2)
        print("\nErro! Senha Incorreta.")
        senha = input("Digite a sua Senha: ")
    else:
        print("\n...")
        time.sleep(2)
        print(f"\nBem Vindo, {nome}\n")

identificação()

def ver_saldo():
    global saldo_atual
    print(f"\nSaldo atual: R$ {saldo_atual:.2f}\n")

hist_saques = []
hist_depositos = []

def sacar():
    global saldo_atual
    valor = float(input("\nInforme o valor de Saque: "))

    if valor <= 500:
        saldo_atual -= valor
        hist_saques.append(valor)
        print(f"Saque de R$: {valor:.2f} realizado com sucesso!\n")
    elif valor > 500:
        print("Error! Somente R$ 500,00 por saque\n")
    else:
        print("Erro! Saldo insuficiente\n")



def depositar():
    global saldo_atual
    deposito = float(input("\nInforme um valor de Depósito: "))
    saldo_atual +=deposito
    hist_depositos.append(deposito)
    print("Depósito realizado!\n ")


def historico_saques():
    if not hist_saques:
        print("Nenhum saque realizado ainda.\n")
    else:
        print("Histórico de Saques:")
        for i, saque in enumerate(hist_saques, 1):
            print(f"{i}. R$ {saque:.2f}")
        print()

def historico_depositos():
    if not hist_depositos:
        print("Nenhum depósito realizado ainda.\n")
    else:
        print("Histórico de Depósitos:")
        for i, deposito in enumerate(hist_depositos, 1):
            print(f"{i}. R$ {deposito:.2f}")
        print()


def sair():
    print("Saindo...")

def main():
    while True:
        print("\nMENU - CAIXA DO BRASIL\n")
        print("[1] Ver saldo")
        print("[2] Sacar")
        print("[3] Depositar \n")
        print("[4] Histórico de Saques")
        print("[5] Histórico de Depósitos\n")
        print("[6] Sair\n")
        escolha = input("Opção: ")

        if escolha == "1":
            ver_saldo()
        elif escolha == "2":
            sacar()
        elif escolha == "3":
            depositar()
        elif escolha == "4":
            historico_saques()
        elif escolha == "5":
            historico_depositos()
        elif escolha == "6":
            sair()
            break
        else:
            print("Opção inválida!\n")


main()

