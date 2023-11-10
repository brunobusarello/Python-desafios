peso = []
pesos = []
numeros = []
maiorp = []
menorp = []
while True:
    peso.append(str(input('Nome: ')))
    peso.append(float(input('Peso: ')))
    continuar = str(input('Quer continuar? [S/N] '))
    pesos.append(peso[:])
    numeros.append(peso[1])
    peso.clear()
    if continuar in 'Nn':
        break
for i, p in enumerate(numeros):
    if i == 0:
        menorp.append(p)
        maiorp.append(p)
    else:
        if p > maiorp[0]:
            maiorp.clear()
            maiorp.append(p)
        if p < menorp[0]:
            menorp.clear()
            menorp.append(p)
for c in pesos:
    if c[1] == maiorp[0]:
        maiorp.append(c[0])
    if c[1] == menorp[0]:
        menorp.append(c[0])
print(f'Foram cadastradas {len(pesos)} pessoas')
print(f'O maior peso foi {maiorp[0]}Kg. Peso de {maiorp[1:]}')
print(f'O menor peso foi {menorp[0]}Kg. Peso de {menorp[1:]}')
