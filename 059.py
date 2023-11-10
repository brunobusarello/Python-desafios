n1 = float(input('Digite o 1° valor: '))
n2 = float(input('Digite o 2° valor: '))

entrada = 0

while entrada != 5:
    print('\n\033[33m[ 1 ] Somar')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Maior')
    print('[ 4 ] Novos números')
    print('[ 5 ] Sair do programa\033[m')
    entrada = int(input('\nDigite a opção que você quer: '))
    if entrada == 1:
        print('\n\033[36m{} + {} = {}\033[m'.format(n1, n2, n1 + n2))
    elif entrada == 2:
        print('\n\033[36m{} X {} = {}\033[m'.format(n1, n2, n1 * n2))
    elif entrada == 3:
        if n1 > n2:
            print('\n\033[36m{} é maior que {}\033[m'.format(n1, n2))
        elif n2 > n1:
            print('\n\033[36m{} é maior que {}\033[m'.format(n2, n1))
    elif entrada == 4:
        n1 = float(input('Digite o 1° valor: '))
        n2 = float(input('Digite o 2° valor: '))
    elif entrada > 5:
        print('\n\033[31mOpção inválida! Tente novamente!\033[m')

print('\033[32mAcabou!\033[m')
