print(30 * '=')
print('\033[36m{:^30}\033[m'.format('10 TERMOS DE UMA PA'))
print(30 * '=')

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1


while cont < 11:
    print('{}'.format(termo), end=' -> ')
    termo += razao
    cont += 1

print('Acabou!')
