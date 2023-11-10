km = float(input('Digite quatos KM foram rodados: '))
if km <= 200:
    k = km * 0.50
    print('Se você andar {}km, você irá pagar R${:.2f}'.format(km, k))
else:
    k = km * 0.45
    print('Se você andar {}km, você irá pagar R${:.2f}'.format(km, k))
