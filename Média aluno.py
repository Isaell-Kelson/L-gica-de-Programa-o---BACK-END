print('======== Avaliação do Aluno ========')


n1 = input('Nome do aluno: ')
n2 = float (input('Primeira nota: '))
n3 = float (input('Segunda nota: '))
n4 = int (input('Faltas: '))

media = (n2 + n3) / 2
print ('Média final: ',media)


if n4 >= 3:
    print('O aluno', n1, 'está REPROVADO POR FALTA!')
elif media <= 6.9:
    print('O aluno ', n1, ' está REPROVADO POR MÉDIA!')
else:
    print('O aluno ', n1, 'está APROVADO POR MÉDIA!')