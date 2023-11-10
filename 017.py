from math import hypot
cat1 = float(input('Digite o cateto oposto: '))
cat2 = float(input('Digite o cateto adjacente: '))
hi = hypot(cat2, cat1)
print('A hipotenusa vai medir {:.2f}'.format(hi))
