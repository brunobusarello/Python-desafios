'''from math import factorial
n = int(input('Digite um número e veja o seu fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')'''

n = int(input('Type a number and see your factorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')


while c > 0:
    print(f'{c}', end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
