cont = 1

while True:
    print('-' * 30)
    n = int(input('Qual tabuada deseja ver? '))
    print('-' * 30)
    if n < 0:
        break
    while cont < 11:
        print(f'{n} X {cont:0>2} = {n * cont}')
        cont += 1
    cont = 1
print('Programa encerrado. Volte sempre!')
