palavras = ('carro', 'pessoa', 'animal', 'jota', 'computador')
for c in range(0, len(palavras)):
    print(f'\n{palavras[c].upper()} tem as seguintes vogais: ', end='')
    if palavras[c].count('a') > 0:
        print('A ' * palavras[c].count('a'), end='')
    if palavras[c].count('e') > 0:
        print('E ' * palavras[c].count('e'), end='')
    if palavras[c].count('i') > 0:
        print('I ' * palavras[c].count('i'), end='')
    if palavras[c].count('o') > 0:
        print('O ' * palavras[c].count('o'), end='')
    if palavras[c].count('u') > 0:
        print('U ' * palavras[c].count('u'), end='')
