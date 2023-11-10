mais18 = homens = mulheres20 = 0


while True:
    idade = int(input('\nDigite a idade: '))
    while True:
        sexo = input('Qual o sexo? ')
        if sexo in 'MmFf':
            break
    print('{:-^30}'.format('CADASTRADO'))
    while True:
        continuar = input('Quer continuar? ')
        if continuar in 'NnSs':
            break
    if idade > 18:
        mais18 += 1
    if sexo == 'm':
        homens += 1
    if sexo == 'f' and idade < 20:
        mulheres20 += 1
    if continuar == 'n':
        break
print('\n{} pessoa{} tem mais de 18 anos'.format(mais18, 's' if mais18 != 1 else ''))
print('{} home{} foram cadastrados'.format(homens, 'ns' if homens != 1 else 'm'))
print(f'{mulheres20} meninas com menos de 20 anos cadastradas')
