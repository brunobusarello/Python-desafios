soma = 0
cont = 0
false = 0
n = 0
while n != 999:
    n = int(input('Digite um número [ 999 para parar ]: '))
    if n != 999:
        soma += n
        cont += 1
    else:
        false += 1
print('Foi digitado {} número{} e a soma deles foi {}'.format(cont, 's' if cont >= 2 else '', soma))
