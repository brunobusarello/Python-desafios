r1 = float(input('Digite o valor de uma reta: '))
r2 = float(input('Digite o valor de outra reta: '))
r3 = float(input('Digite um outro valor de outra reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com os três segmentos é possível formar um triângulo', end=' ')
    if r1 == r2 and r1 == r3 and r3 == r2:
        print('EQUILÁTERO')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('Não é possível formar um triângulo com os três segmentos')