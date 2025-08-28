import random
musica = []

for i in range(5):
    nome_musica = input(f"Informe a Música {i+1}: ")
    musica.append(nome_musica)

musica_sorteada = random.choice(musica)
print()
print(f"Tocando agora: {musica_sorteada}")


