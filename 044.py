from time import sleep
print('{:-^40}'.format('\033[36m MY STORE \033[m'))
print(' ')
valor = float(input('Qual o valor do produto? '))
sleep(1.3)
print(' ')
print('\033[33mSe você quer pagar à vista, digite 1')
print('Se você quer pagar à vista no cartão, digite 2')
print('Se você quer pagar em até 2x no cartão, digite 3')
print('Se você quer pagar em 3x ou mais no cartão, digite 4\033[m')
print(' ')
sleep(1.3)
fpgto = int(input('Qual será a forma de pagamento?'))

sleep(2)

if fpgto == 1:
    v = valor * 90 / 100
    print('Você teve 10% de desconto! Você irá pagar R${:.2f}'.format(v))
elif fpgto == 2:
    v = valor * 95 / 100
    print('Você teve 5% de desconto! Você irá pagar R${:.2f}'.format(v))
elif fpgto == 3:
    print('Não conseguimos desconto, o valor continou igual')
elif fpgto == 4:
    v = valor * 120 / 100
    parc = int(input('Em quantas vezes? '))
    vparc = v / parc
    print('Sua compra será parcelada em {} vezes de R${:.2f}'.format(parc, vparc))
    print('Você terá que pagar 20% a mais, o valor ficará R${:.2f}'.format(v))
else:
    print('Não possuímos esta forma de pagamento')
