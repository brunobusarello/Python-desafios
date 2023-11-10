gols = []
dados = {}
tot = 0
dados['Nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'   Quantos gols na partida {c}? ')))
    tot += gols[c]
dados['Gols'] = gols[:]
dados['Total'] = sum(gols)
print('\033[36m-=\033[m' * 30)
print(dados)
print('\033[36m-=\033[m' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('\033[36m-=\033[m' * 30)
print(f'O jogador {dados["Nome"]} jogou {len(dados["Gols"])} partidas')
for i, v in enumerate(dados['Gols']):
    print(f'    => Na partida {i}, fez {v} gols')
print(f'Foi um total de {dados["Total"]} gols')
