palavras = ('carro', 'pessoa', 'animal', 'jota', 'computador')
for c in palavras:
    print(f'\n{c.upper()} tem as seguintes vogais: ', end='')
    for p in c:
        if p.lower() in 'aeiou':
            print(p, end=' ')
