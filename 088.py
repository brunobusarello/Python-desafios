from time import sleep
from random import randint
lista = []


print('-' * 30)
print('{:^30}'.format('JOGA NA SENA'))
print('-' * 30)

jogar = int(input('Quantos jogos você quer sortear? '))
for c in range(0, jogar):
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
        if len(lista) == 6:
            break
    lista.sort()
    print(f'Jogo {c + 1}: {lista}')
    sleep(1)
    lista.clear()
