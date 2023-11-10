from random import randint
from time import sleep
from operator import itemgetter
jogo = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}
ranking = []

print(f'\033[36m{" Valores sorteados: ":-^30}\033[m')
for k, v in jogo.items():
    print(f'{k} tirou o {v} no dado.')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
sleep(1)
print()
print(f'\033[36m{" Ranking: ":-^30}\033[m')
sleep(1)
for i, v in enumerate(ranking):
    print(f'{i + 1}° lugar: {v[0]} com {v[1]}')
    sleep(0.5)
