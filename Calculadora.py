import os
import time 

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def somar():
    try:
        n1 = int(input("\nDigite o Primeiro Numero: "))
        n2 = int(input("Digite o Segundo Número: "))
        somar = (n1 +n2)
        print(f"\nResposta: {somar}\n")
    except:
        print("Valor inválido")


def subtrair():
    try:
        n1 = int(input("\nDigite o Primeiro Numero: "))
        n2 = int(input("Digite o Segundo Número: "))
        sub = (n1 - n2)

        while sub < 0:
            print("\nApenas Números Positivos! Tente Novamente")
            n1 = int(input("\nDigite o Primeiro Numero: "))
            n2 = int(input("Digite o Segundo Número: "))
            sub = n1 - n2 

        print(f"\nResposta: {sub}\n")
    except:
        print("Valor inválido")

def multiplicação():
    try: 

        n1 = int(input("\nDigite o Primeiro Numero: "))
        n2 = int(input("Digite o Segundo Número: "))
        mult = (n1 *n2)
        print(f"\nResposta: {mult}\n")
    except:
        print("Valor Ìnvalido")

def sair():
    print("\nAte Logo...\n")

def calculadora():
    while True:
        clear()
        print("CALCULADORA\n")
        print("[1] - Soma")
        print("[2] - Subtração")
        print("[3] - Multiplicação")
        print("[0] - Sair\n")
        opção = input("Insira sua Opção: ")

        if opção == "1":
            somar()
            time.sleep(2)
        elif opção == "2":
            subtrair()
            time.sleep(2)
        elif opção == "3":
            multiplicação()
            time.sleep(2)
        elif opção == "0":
            sair()
            break
        else:
            print("Opção ìnvalida")
            time.sleep(2)

calculadora()









