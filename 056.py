soma = 0
homem = 0
nhomem = ''
cont = 0
for p in range(1, 5):
    print('----- {}° PESSOA -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    soma += idade
    if sexo in 'Mm':
        if p == 1:
            homem = idade
            nhomem = nome
        else:
            if idade > homem:
                homem = idade
                nhomem = nome
    else:
        if p == 1:
            if idade < 20:
                cont += 1
        else:
            if idade < 20:
                cont += 1

print('\nA média de idade do grupo é {:.2f}'.format(soma / 4))
print('O homem mais velho tem {} anos e se chama {}'.format(homem, nhomem))
print('Tem {} mulheres com menos de 20 anos'.format(cont))
