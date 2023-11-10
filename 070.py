menorvalor = cont = soma = produtos1000 = 0
nomemenor = ''
print('-' * 45)
print('{:^45}'.format('LOJINHA DA 25'))
print('-' * 45)
while True:
    nome = str(input('\nQual o nome do item: '))
    valor = float(input('Qual o preço do item? R$'))
    print('-' * 30)
    soma += valor
    if valor > 1000:
        produtos1000 += 1
    if cont == 0:
        nomemenor = nome
        menorvalor = valor
    else:
        if valor < menorvalor:
            menorvalor = valor
            nomemenor = nome
    cont += 1
    while True:
        continuar = input('Quer adicionar mais itens? ').strip().upper()[0]
        if continuar in 'SN':
            break
    if continuar in 'N':
        break

print(f'\nForam gastos R${soma:.2f}')
print(f'{produtos1000} itens custam mais de R$1000,00')
print(f'{nomemenor} é o produto mais barato, custando R${menorvalor:.2f}')
