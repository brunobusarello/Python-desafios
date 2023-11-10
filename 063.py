print(30 * '=')
print('\033[36m{:^30}\033[m'.format('Seq. FIBONACCI'))
print(30 * '=')
n = int(input('Digite quantos números você quer ver: '))
cont = 3
t1 = 0
t2 = 1

print(f'{t1}', end=' -> ')
print(f'{t2}' if n >= 2 else 'Fim', end=' -> ')
while cont <= n:
    resultado = t1 + t2
    print('{}'.format(resultado), end=' -> ')
    t1 = t2
    t2 = resultado
    cont += 1
print('Fim' if n >= 2 else '')
