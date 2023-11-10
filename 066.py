
soma = valores = 0
while True:
    n = int(input('Digite um valor [ 999 para ]: '))
    if n == 999:
        break
    soma += n
    valores += 1
if valores > 1:
    print(f'A soma dos {valores} valores deu {soma}')
else:
    print('Só tem um valor, logo a soma é ele mesmo')
