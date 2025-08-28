def gerar_Um_Tabuleiro(n):
    for i in range(n):
        linha = ""
        for j in range(n):
            if (i + j ) %2 == 0:
                linha+= " X "
            else:
                linha += " O "
        print(linha)

num = int(input("Digite o tamanho do Tabuleiro: "))
gerar_Um_Tabuleiro(num)