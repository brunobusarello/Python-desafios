from random import randint
aleatorio = randint(0, 10)
cont = 1

print('-*' * 20)
print('{:^40}'.format(' Digite um valor de 0 a 10 '))
print('-*' * 20)

valor = int(input('Valor: '))

while valor != aleatorio:
    if valor > aleatorio:
        print('Menos! Try again!')
    elif aleatorio > valor:
        print('Mais! Try again!')
    valor = int(input('Valor: '))
    cont += 1

print('Parabéns, você acertou!')
print('Foram necessárias {} tentativas'.format(cont))
