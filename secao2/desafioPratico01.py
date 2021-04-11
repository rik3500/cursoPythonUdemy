nome = str(input('Digite o nome do aluno: '))
idade = int(input('Digite a idade do aluno: '))
prova1 = float(input('Digite a nota N1 do aluno: '))
prova2 = float(input('Digite a nota N2 do aluno: '))

nome = nome.lower().title()
print('O nome do aluno é {}'.format(nome))

mediaProva = (prova1+prova2)/2
print('A média do aluno é {}'.format(mediaProva))

if mediaProva>=6 and idade>=18:
    print('O aluno está aprovado.')
else:
    print('O aluno está reprovado')