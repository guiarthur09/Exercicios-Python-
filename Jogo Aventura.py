import random

def inicio():
    direcoes = []
    recompensas = [
        "Poção de cura",
        "Espada rara",
        "Armadura mágica",
        "Anel de invisibilidade",
        "Pergaminho de feitiço"
    ]

    for i in range(10):
        direcao = input("Em que direção você quer ir agora? (cima, baixo, esquerda, direita): ").strip().lower()

        while direcao not in ["cima", "baixo", "esquerda", "direita"]:
            direcao = input("Direção inválida! Digite novamente (cima, baixo, esquerda, direita): ").strip().lower()

        direcoes.append(direcao)

    if direcoes[9] == "cima":
        indice_recompensa = random.randint(0, 4)
        print("\nParabéns! Você encontrou um baú de tesouro!")
        print("Sua recompensa é:", recompensas[indice_recompensa])
    else:
        print("\nOh não! Você encontrou um inimigo poderoso!")
        print("Infelizmente você não tem força suficiente...")
        print("Você foi derrotado em combate.")

    print("\nCaminho percorrido:")
    for i in range(10):
        print(f"{i + 1}ª direção: {direcoes[i]}")

inicio()
