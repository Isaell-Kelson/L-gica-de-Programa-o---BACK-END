import pandas as pd

df_alunos = pd.read_csv('notas_alunos.csv')

media = (df_alunos['nota_1'] + df_alunos['nota_2']) / 2
df_alunos['Media'] = media

df_alunos.loc[df_alunos['Media'] >= 7, 'Situação'] = 'Aprovado'
df_alunos.loc[df_alunos['Faltas'] > 5, 'Situação'] = 'Reprovado'
df_alunos.loc[df_alunos['Media'] < 7, 'Situação'] = 'Reprovado'
print(df_alunos)
print('')
df_alunos.to_csv('alunos_situacao.csv')

faltoso = df_alunos['Faltas'].max()
print('O aluno que possui maior número de faltas é: '+str(faltoso))
print('')
mg = df_alunos['Media'].median()
print('A media geral foi de: '+str(mg))
print('')
ma = df_alunos['Media'].max()
print('O aluno com a maior média foi: '+str(ma))