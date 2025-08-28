import time

estoque = []

def cadastrarBike():
    nome = input("Bicicleta: ")
    preço = float(input("Preço: "))
    qtd = int(input("Quantidade: "))

    poduto = {'Nome': nome, 'Preço': preço, 'Quantidade': qtd}
    estoque.append(poduto)
    print()
    print("Cadastrando Produto...")
    print()
    time.sleep(3)
    print("Analisando...")
    print()
    time.sleep(2)
    print("Produto Cadastrado !!\n")

def listarProdutos():
        if len(estoque) == 0:
            print("...")
            print()
            time.sleep(2)
            print("Nenhum produto cadastrado.\n")
            return

        for i, produto in enumerate(estoque, 1):
            nome = produto["Nome"]
            preco = produto["Preço"]
            quantidade = produto["Quantidade"]
            print(f"Produto {i}: {nome} | Preço: R$ {preco:.2f} | Quantidade: {quantidade}")
            print()

def sair():
    print("Encerrado. ")

def main():
    while True:
            
        print(" ----- MENU BIKES -----\n")
        print("[1] Cadastrar Produto")
        print("[2] Listar Produtos")
        print("[3] Sair\n")
        escolha = int(input("Escolha: "))
        print()

        if escolha == 1:
            cadastrarBike()
        if escolha == 2:
            listarProdutos()
        if escolha == 3:
            sair()
            break
        if escolha >= 4 or escolha <=0:
            print("Opção ìnvalida!")
            print()
        
main()
        



