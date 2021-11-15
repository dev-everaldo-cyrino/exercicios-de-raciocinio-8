totaldia = []
estrato = 0
def pagar(conta,dia):
    dia *=  0.001
    dia += 0.03
    juros = conta
    juros *=  dia
    total = conta + juros
    print('sua conta total é de {}'.format(total))
    print('..............................')
    totaldia.append(total)
    
while True:
    conta = float(input('valor da conta: '))
    if conta == 0:
        for x in range(len(totaldia)):
            estrato += totaldia[x]
        print('total pago hoje é de {}'.format(estrato))
        break
    dia = int(input('dias de atraso: '))
    pagar(conta,dia)
    