times = ('botafogo', 'flamengo', 'gremio', 'fluminense', 'palmeiras', 'bragantino', 'fortaleza',
         'são paulo', 'cruzeiro', 'internacional', 'atletico-pr', 'atletico-mg', 'santos', 'cuiaba',
         'corinthians', 'bahia', 'goias', 'coritiba', 'vasco', 'américa-mg')
print(f'Os 5 primeiros colocados são:')
for c in times[:5]:
    print(c, end=', ')
print(f'\nOs 4 lanterninhas são: {times[-4:]}')
print(sorted(times))

print('Fortaleza se encontra na {}° posição'.format(times.index('fortaleza') + 1))
