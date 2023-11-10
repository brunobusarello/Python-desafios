r1 = float(input('Digite o valor de uma reta: '))
r2 = float(input('Digite o valor de outra reta: '))
r3 = float(input('Digite um outro valor de outra reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível formar um triângulo com os três segmentos')
else:
    print('Não é possível formar um triângulo com os três segmentos')
