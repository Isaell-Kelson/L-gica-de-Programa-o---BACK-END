print('Vamos te ajudar a escolher a melhor categoria de acordo com o seu veículo')
print("")

qr = int (input('Quantidade de rodas: '))
pb = float (input('Peso bruto em Kg: '))
qp = int (input('Quantidaded e pessoas no veículo: '))
print("")

if qr == 2 and 3:
    print('A melhor categoria para você é "A"!')
elif qr == 4 and qp <= 8 and pb <= 3500:
    print('A melhor categoria para você é "B"!')
elif qr >= 4 and pb >= 3500 and pb <= 6000:
    print('A melhor categoria para você é a "C"!')
elif qr >= 4 and qp > 8:
    print('A melhor categoria para você é a "D"!')
elif qr >= 4 and pb >= 6000:
    print('A melhor categoria para você é a "E"!')