vel = float(input('Digite a velocidade do veículo: '))
if vel > 80:
    multa = (vel - 80) * 7
    print('Você foi MULTADO, deverá pagar R${:.2f}'.format(multa))
else:
    print('PARABÉNS! você estava dentro da velocidade permitida!')