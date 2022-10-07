import enum

voto = 'não'
encerrar = 'não'
x = 0
y = 0
z = 0
b = 0
nulo = 0

class candidatos(enum.Enum):
    Candidato_X = 889
    Candidato_Y = 847
    Candidato_Z = 515
    Branco = 0
total = 0

while (encerrar == 'não'):
    voto = 'não'
    while(voto == 'não'):
        print('Digite o número do candidato: ')
        
        try:
            votos = int(input())
            voto = str(input('Deseja confirmar seu voto? '))
            if(votos == 889):
                x = x + 1
            elif(votos == 847):
                y = y + 1
            elif(votos == 515):
                z = z + 1
            elif(votos == 0):
                b = b + 1
            else:
                nulo = nulo + 1

        except:
            print('Dígito incorreto!')
    print('Voto confirmado!')
    encerrar = (input('Encerrar votação? '))
print('FIM')
print('')

if(x > y) and (x > z):
    mv = x
    mcandidato = candidatos.Candidato_X
elif(y > x) and (y > z):
    mv = y
    mcandidato = candidatos.Candidato_Y
elif(z > x) and (z > y):
    mv = z
    mcandidato = candidatos.Candidato_Z

cx = candidatos.Candidato_X
cy = candidatos.Candidato_Y
cz = candidatos.Candidato_Z
br = candidatos.Branco   

    
print('O candidato vencedor é: ', mcandidato.name,' com o total de ',mv, ' votos')
print('O candidato_X', cx.name,' recebeu', x, 'votos')
print('O candidato_Y', cy.name,' recebeu', y, 'votos')
print('O candidato_Z', cz.name,' recebeu', z, 'votos')
print('O total de votos em', br.name,' foram de ',br)
print('O total de votos Nulos foram de ',nulo)