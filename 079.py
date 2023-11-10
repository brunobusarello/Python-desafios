valores = []
while True:
    v = int(input('Digite um valor: '))
    if v not in valores:
        valores.append(v)
        print('Valor adicionado')
    else:
        print('Valor duplicado')
    continuar = str(input('Quer continuar? '))
    if continuar in 'Nn':
        break
valores.sort()
print(f'Foram digitados os valores {valores}')
