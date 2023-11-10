frs = str(input('Digite uma frase: ')).strip().upper()
print('A frase {} tem {} caracteres "A"'.format(frs, frs.count('A')))
print('A primeira letra "A" aparece na posição {}'.format(frs.find('A') + 1))
print('A última letra "A" aparece na posição {}'.format(frs.rfind('A') + 1))
