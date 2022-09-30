print('          ---- Insira seu nome e ano de nascimento para sabermos sua idade ----')
print('')
rodar = True
while(rodar==True):

    try:
        print('Digite o seu nome: ')
        
    
        nome = str(input())
        print('')

        print('Ano de nascimento: ')
        

        nasc = int(input())
        print('')

        
        ano2 = 2022

        if nasc >= 1922 and nasc <= 2022:
            res = ano2 - nasc
            print('Você é: ',nome)
            print('Sua idade é: ',res)

        rodar = False

    except:
        print('Dados incorretos')

print('Finalizado')
