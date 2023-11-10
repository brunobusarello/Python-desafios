peso = []
pesos = []
maior = menor = 0
while True:
    peso.append(str(input('Nome: ')))
    peso.append(float(input('Peso: ')))
    if len(pesos) == 0:
        maior = menor = peso[1]
    else:
        if peso[1] > maior:
            maior = peso[1]
        if peso[1] < menor:
            menor = peso[1]
    pesos.append(peso[:])
    peso.clear()
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break
print(f'Foram cadastradas {len(pesos)} pessoas')
print(f'O maior peso foi {maior}Kg. Peso de ', end='')
for p in pesos:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi {menor}Kg. Peso de ', end='')
for p in pesos:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()
