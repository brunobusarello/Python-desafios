from random import randint

cont = 0

print('-_' * 15)
print('\033[36m{:^30}\033[m'.format('PAR OU ÍMPAR'))
print('-_' * 15)

while True:
    
    num = int(input('Digite um valor: '))
    while True:
        parimpar = str(input('Par ou Ímpar? [ p/i ] ')).strip().lower()[0]
        if parimpar in 'PIpi':
            break

    computador = randint(0, 10)
    resultado = computador + num
    resto = resultado % 2

    print(f'\nVocê jogou {num} e o PC {computador}. Total de {resultado} deu ', end='')
    print('ÍMPAR' if resto == 1 else 'PAR')

    print('-_' * 15)
    if resto == 1:
        if parimpar == 'p':
            print('\033[31mVocê perdeu\033[m')
            break
        else:
            print('\033[32mVocê venceu\033[m')
            cont += 1
    if resto == 0:
        if parimpar == 'i':
            print('\033[31mVocê perdeu\033[m')
            break
        else:
            print('\033[32mVocê venceu\033[m')
            cont += 1
    print('-_' * 15)
    print('\nVamos jogar novamente')

print('\nGAME OVER. Você venceu {} vez{}'.format(cont, 'es' if cont != 1 else ''))
