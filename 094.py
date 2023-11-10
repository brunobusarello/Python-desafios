temp = {}
lista = []
tot = 0
media = 0
mulheres = []
while True:
    temp['Nome'] = str(input('Nome: '))
    while True:
        temp['Sexo'] = str(input('Sexo: ')).upper()[0]
        if temp['Sexo'] in 'MmFf':
            break
        print('ERRO! Por favor, digite apenas F ou M')
    temp['Idade'] = int(input('Idade: '))
    lista.append(temp.copy())
    while True:
        continuar = str(input('Quer continuar? [S / N]'))
        if continuar in 'SsNn':
            break
        print('ERRO! Digite apenas S ou N')
    if continuar in 'Nn':
        break
print('\033[36m-=\033[m' * 30)
print(f' - Foram cadastradas {len(lista)} pessoas')
for v in lista:
    tot += v['Idade']
    if v['Sexo'] == 'F':
        mulheres.append(v['Nome'])
media = tot / len(lista)
print(f' - A média de idade é {media:.2f}')
if len(mulheres) > 0:
    print(' - As mulheres cadastradas foram: ', end='')
    for v in mulheres:
        print(v, end='  ')
    print()
else:
    print('\033[31m - Nenhuma mulher foi cadastrada\033[m')

print(' - Lista das pessoas que estão acima da média: ')
for n in lista:
    print('    ')
    if n['Idade'] >= media:
        for k, v in n.items():
            print(f'{k} = {v}; ', end='')
    print()
print()
