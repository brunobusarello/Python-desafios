from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
menor = maior = numeros[0]
print('Número sorteados: ', end='')
for c in range(0, len(numeros)):
    print(numeros[c], end=' ')
    if numeros[c] > maior:
        maior = numeros[c]
    if numeros[c] < menor:
        menor = numeros[c]
# print(f'\nO menor número é o {menor}')
# print(f'O maior número é o {maior}')
print(f'\nO maior valor foi {max(numeros)}')
print(f'O menor valor foi {min(numeros)}')

