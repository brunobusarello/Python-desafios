print(30 * '=')
print('\033[36m{:^30}\033[m'.format('10 TERMOS DE UMA PA'))
print(30 * '=')

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais > 0:
    total += mais

    while cont <= total:
        print('{}'.format(termo), end=' -> ')
        termo += razao
        cont += 1

    print('Pausa!')
    mais = int(input('Quantos termos a mais? '))
print('Fim')
print('Foram mostrados {} números'.format(cont - 1))
