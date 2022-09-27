operacao = input('Digite a operação que você deseja (soma, subtração, multiplicação, divisão): ')
n1 = int (input('Digite um número: '))
n2 = int (input('Digite outro número: '))

if operacao == 'soma':
    resultado = n1 + n2

elif operacao == 'subtração':
    resultado = n1 - n2

elif operacao == 'multiplicação':
    resultado = n1 * n2

elif operacao == 'divisão':
    resultado = n1 / n2

else:
    resultado = '0'  


print ('O resultado da operação é: ', resultado)