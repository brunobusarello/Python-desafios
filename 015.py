km = int(input('Quantos quilômetros foram rodados? '))
dias = int(input('Quantos dias o carro foi usado? '))
v1 = km * 0.15
v2 = dias * 60
print('O total a pagar de aluguel foi de R${:.2f}'.format(v2 + v1))
