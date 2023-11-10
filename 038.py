n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
if n1 > n2:
    print('\033[32m{}\033[m é maior que \033[31m{}\033[m'.format(n1, n2))
elif n2 > n1:
    print('\033[32m{}\033[m é maior que \033[31m{}\033[m'.format(n2, n1))
elif n1 == n2:
    print('Os valores {} e {} são iguais'.format(n1, n2))
else:
    print('\033[31mNão consigo comparar os números. Tente novamente\033[m')
