numeros = (int(input('Digite um valor: ')),
            int(input('Digite um valor: ')),
            int(input('Digite um valor: ')),
            int(input('Digite um valor: ')))

print('Os 4 valores são: ', end='')
for c in range(0, len(numeros)):
    print(numeros[c], end=' ')
print('\nO número nove ( 9 ) apareceu {} vezes'.format(numeros.count(9)))
if numeros.count(3) > 0:
    print('O número três ( 3 ) está na {}° posição'.format(numeros.index(3) + 1))
else:
    print('O número três ( 3 ) não foi digitado')
print('Os números pares foram: ', end='')
for c in range(0, len(numeros)):
    if numeros[c] % 2 == 0:
        print(numeros[c], end=' ')
