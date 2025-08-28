import time

usuario_cadastrado = ""
senha_cadastrada = ""

def cadastrar():
    global usuario_cadastrado, senha_cadastrada
    usuario_cadastrado = input("Usuário Novo: ")
    
    senha_cadastrada = input("Senha Nova: ")
    print()
    print("Cadastro Realizado.")
    print()

def login():
    if usuario_cadastrado == "" or senha_cadastrada == "":
        print("Nenhum usuário cadastrado ainda. Cadastre-se primeiro.")
        print()
        return

    usuario = input("Usuário: ")
    senha = input("Senha: ")
    
    if usuario == usuario_cadastrado and senha == senha_cadastrada:
        print("Login realizado com sucesso!")
        print()
    else:
        print("Usuário ou senha incorretos.")
        print()

def sair():
    print("Programa Encerrado.")
    exit()

def menu_principal():
    while True:
        print("----- Sistema de Login -----")
        print("1 - Cadastrar")
        print("2 - Login")
        print("3 - Sair")
        print()
        op = input("Escolha: ")
        print()

        if op == "1":
            cadastrar()
        elif op == "2":
            login()
        elif op == "3":
            sair()
        else:
            print("Opção inválida.")
            print()

menu_principal()
