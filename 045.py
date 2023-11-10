from random import choice
from time import sleep
print('Jogue JOKENPÔ comigo, digite P para PEDRA, F para PAPEL e T para TESOURA')
sleep(1.2)
resposta = str(input('E aí? Pedra, papel ou tesoura? ')).strip().upper()
sleep(1.2)

lista = ['PEDRA', 'PAPEL', 'TESOURA']
comres = choice(lista)

if resposta == 'PAPEL' and comres == 'PEDRA':
    print('Você ganhou, pois joguei {}'.format(comres))
elif resposta == 'PAPEL' and comres == 'TESOURA':
    print('Ganhei! Eu joguei {}'.format(comres))
elif resposta == 'PEDRA' and comres == 'TESOURA':
    print('Você ganhou, pois joguei {}'.format(comres))
elif resposta == 'PEDRA' and comres == 'PAPEL':
    print('Ganhei! Eu joguei {}'.format(comres))
elif resposta == 'TESOURA' and comres == 'PAPEL':
    print('Você ganhou, pois joguei {}'.format(comres))
elif resposta == 'TESOURA' and comres == 'PEDRA':
    print('Ganhei! Eu joguei {}'.format(comres))
else:
    print('Empatamos')
