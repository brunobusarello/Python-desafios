valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break
print(f'Foram digitados {len(valores)} números')
valores.sort(reverse=True)
print(f'A lista dos valores em ordem decrescente é: {valores}')
cont = 0
while cont < len(valores):
    if valores[cont] == 5:
        print('O valor 5 está na lista')
        break
    else:
        if cont + 1 == len(valores):
            print('O valor 5 não está na lista')
    cont += 1
