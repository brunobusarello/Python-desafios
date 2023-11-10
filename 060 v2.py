n = int(input('Digite um número e veja o seu fatorial: '))
f = 1

for c in range(n, 0, -1):
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')
    f *= c
print('{}'.format(f))
