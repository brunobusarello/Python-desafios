from time import sleep


def contagem(inicio, fim, passo):
    total = 0
    print('\033[36m-=\033[m' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo < 0:
        passo = -passo
    if passo == 0:
        passo = 1
    if fim > inicio:
        total = inicio - passo
        while total < fim:
            total += passo
            print(total, end='   ')
            sleep(0.25)
    if inicio > fim:
        total = inicio + passo
        while total - passo >= fim:
            total -= passo
            print(total, end='   ')
            sleep(0.25)
        total = 0
    print('FIM!')
    print()


contagem(1, 10, 1)
contagem(10, 0, 2)
print('\033[36m-=\033[m' * 30)
print(f'{" Sua vez ":-^60}')
i = int(input('Início: '))
f = int(input('Fim:    '))
p = int(input('Passo:  '))
contagem(i, f, p)
