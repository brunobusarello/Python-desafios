sal = float(input('Digite o salário: '))
cores = {'verde': '\033[1;42m',
         'vermelho': '\033[1;31m',
         'limpa': '\033[m'}
if sal > 1250:
    s = sal * 110 / 100
    print('O salário que antes era {}R${:.2f}{}, ficará {}R${:.2f}{} com o reajuste de 10%'.format(cores['vermelho'], sal, cores['limpa'], cores['verde'], s, cores['limpa']))
else:
    s = sal * 115 / 100
    print('O salário que antes era {}R${:.2f}{}, ficará {}R${:.2f}{} com o reajuste de 15%'.format(cores['vermelho'], sal, cores['limpa'], cores['verde'], s, cores['limpa']))
