def complexo():
   opc = 1

print('              ********* Escolha abaixo qual operação matemática você deseja fazer e em seguida digite os números *********')
print('')
while(True):

       print('''       1 - Adição 
       2 - Subtração 
       3 - Multiplicação 
       4 - Divisão 
       0 - Sair''')
       print('')
       opc = int(input(str('Qual é a sua opção? ')))


       if (opc < 1 or opc > 4): 
            print('Calculadora encerrada')
            break

       print("\nPrimeiro número:\n")
       a = complex(input())

       print("\nSegundo número:\n")
       b = complex(input())

       print("\nTerceiro número:\n")
       c = complex(input())


       if(opc == 1):
           soma = (a + b + c)
           print(soma,"Propriedade Real: ", soma.real,"Propriedade Imaginária: ",soma.imag)


       elif(opc == 2):
           sub = (a - b - c)
           print(sub,"Propriedade Real: ", sub.real,"Propriedade Imaginária: ",sub.imag)


       elif(opc == 3):
           mul = (a * b * c)
           print(mul,"Propriedade Real: ", mul.real,"Propriedade Imaginária: ",mul.imag)


       elif(opc == 4):
           div = (a / b / c)
           print(div,"Propriedade Real: ", div.real,"Propriedade Imaginária: ",div.imag)


       print ("\n\n")

complexo()
