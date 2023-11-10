
while True:
    print('-' * 30)
    n = int(input('Qual tabuada deseja ver? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} X {c:0>2} = {n * c}')
print('Programa encerrado. Volte sempre!')
