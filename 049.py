n = int(input('Digite a sua tabuada: '))
for c in range(1, 11):
    print('{} X {:0>2} = {:0>2}'.format(n, c, n*c))
