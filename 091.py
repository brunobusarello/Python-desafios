from random import randint
from time import sleep
jogadores = {}
lista = []
organized = []
cont = 0
print('Valores sorteados')
for c in range(1, 5):
    jogadores['jogador'] = randint(1, 6)
    lista.append(jogadores.copy())
for k, v in enumerate(lista):
    for n in v.values():
        print(f'    O jogador{k + 1} tirou {n}')
    sleep(0.5)
print('Ranking dos jogadores: ')
print(lista)
