from time import sleep
print('{}Insira alguns dados para ver se a compra da casa será aprovada{}'.format('\033[7;36m', '\033[m'))
sleep(2)
sal = float(input('\033[33mDigite o seu salário: R$ '))
casa = float(input('\033[33mDigite o valor da casa: R$ '))
anos = float(input('\033[33mEm quantos anos irá pagar a casa? \033[m'))

am = anos * 12
prest = casa / am
sal30 = sal * 30 / 100

if prest > sal30:
    print('\033[31mInfelizmente, você não pode comprar essa casa\033[m')
else:
    print('\033[32mVocê pode comprar essa casa!\033[m')
print('30% do seu salário é {}'.format(sal30))
print('A parcela mensal da casa é R${:.2f}'.format(prest))
