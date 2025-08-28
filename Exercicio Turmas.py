turma = 0
soma_medias = 0
total_alunos = 0

while turma < 5:
    print(f"\nTurma {turma+1}")

    alunos = int(input("Quantos Alunos há em cada Turma? "))

    acima_deSete = 0
    cont = 0

    while cont < alunos:
        media_aluno = float(input(f"Informe a Média do Aluno {cont+1} : "))

        soma_medias += media_aluno
        total_alunos+=1

        if media_aluno >= 7:
            acima_deSete +=1
            
            soma_medias += media_aluno
            cont+=1

    turma+=1
    total_alunos +=alunos

print(f"\nTotal de Alunos com Média >= 7: {turma} {acima_deSete} ")

midia_geral = soma_medias / total_alunos

print(f"\nMédia Geral da Escola: {midia_geral:.2f}")
        