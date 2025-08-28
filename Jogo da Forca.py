palavra = "python"
base = ["_", "_","_","_","_","_"]

letras_errada = []

tentativas = 6
erro = 0

while erro < tentativas:
    print(f"\nPalavra: {' '.join(base)}")
    letra = input("Digite uma Letra: ").lower()  

    if letra in palavra:
        for i in range(len(palavra)):
            if palavra[i] == letra:
                base[i] = letra
        print("Acertou!")
    else:
        if letra not in letras_errada:  
            letras_errada.append(letra)
            erro += 1
        print("Errou!")
        print(f"Letras erradas: {', '.join(letras_errada)}")
        print(f"Erros: {erro} de {tentativas}")

    if "_" not in base:
        print(f"\nParabéns! Você ganhou! A palavra era: {palavra}")
        break
else:
    print(f"\nOps! Você perdeu! A palavra era: {palavra}")

  
  