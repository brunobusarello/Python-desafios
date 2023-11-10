from random import randint
from time import sleep
print('<>=_=<>' * 10)
num = int(input('Digite um valor entre 0 e 5: '))
print('<>=_=<>' * 10)
n = randint(0, 5)
print('PROCESSANDO...')
sleep(1)
if num == n:
    print('PARABÉNS! você acertou o valor que pensei!')
else:
    print('Você errou, tente de novo')
    print('O valor que pensei era: {}'.format(n))

