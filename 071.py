cont50 = cont20 = cont10 = cont1 = 0
print('=' * 30)
print('{:^30}'.format('BANCO BRUNELSON'))
print('=' * 30)

valor = int(input('Digite o valor a ser sacado: R$'))

while True:
    if valor >= 50:
        valor -= 50
        cont50 += 1
    elif valor >= 20:
        valor -= 20
        cont20 += 1
    elif valor >= 10:
        valor -= 10
        cont10 += 1
    elif valor >= 1:
        valor -= 1
        cont1 += 1
    else:
        break

if cont50 > 0:
    print(f'{cont50} cédulas de R$50')
if cont20 > 0:
    print(f'{cont20} cédulas de R$20')
if cont10 > 0:
    print(f'{cont10} cédulas de R$10')
if cont1 > 0:
    print(f'{cont1} cédulas de R$01')
print('=' * 30)
print('Volte sempre a rede de Bancos BRUNELSON')
