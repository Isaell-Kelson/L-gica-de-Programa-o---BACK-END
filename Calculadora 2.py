print('          -------Para fazer sua operação escolha uma das opções a seguir-------')
print('')
print('0. Sair')
print('1. Somar')
print('2. Subtrair')
print('3. Multiplicação')
print('4. Divisão')
print('')

def soma():

    n1 = float(input('Primeiro número: '))
    n2 = float(input('Segundo número: '))
    return(print('Soma = ',n1 + n2))

def subtração():

    n1 = float(input('Primeiro número: '))
    n2 = float(input('Segundo número: '))
    return(print('Subtração = ', n1 - n2))

def multiplicação():

    n1 = float(input('Primeiro número: '))
    n2 = float(input('Segundo número: '))
    return(print('Multiplicação = ', n1 * n2))

def divisão():
    n1 = float(input('Primeiro número: '))
    n2 = float(input('Segundo número: '))
    return(print('Divisão = ', n1 / n2))



opcao = 0


while opcao:
    
    
    

    
    print('0. Sair')
    print('1. Somar')
    print('2. Subtrair')
    print('3. Multiplicação')
    print('4. Divisão')
    


opcao = int(input('Opção: '))



if(opcao == 0):
    print('----Você saiu da calculadora---')
elif(opcao == 1):
    soma()
elif(opcao == 2):
    subtração()
elif(opcao == 3):
    multiplicação()
elif(opcao == 4):
    divisão()

else:
    print('Essa opção não existe!')    