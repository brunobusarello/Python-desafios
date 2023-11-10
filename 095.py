gols = []
dados = {}
tot = 0
jogadores = []
while True:
    print('-' * 45)
    dados['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {dados["Nome"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'   Quantos gols na partida {c + 1}? ')))
        tot += gols[c]
    dados['Gols'] = gols[:]
    dados['Total'] = tot
    jogadores.append(dados.copy())
    gols.clear()
    while True:
        continuar = str(input('Quer continuar? [S/N]'))
        if continuar in 'SsnN':
            break
        print('ERRO! Responda apenas S ou N')
    if continuar in 'Nn':
        break
    tot = 0
print('\033[36m-=\033[m' * 30)
print(f'{"Cód.":>5} {"Nome":<16} {"Gols":<20} {"Total":^5}')
print('-' * 50)
for i, n in enumerate(jogadores):
    print(f'{i:<5} {n["Nome"]:<16} {str(n["Gols"]):<20} {n["Total"]:^5}')
print('\033[36m-=\033[m' * 30)
while True:
    show = int(input('Mostrar dados de qual jogador? (999 para o programa)'))
    print('-' * 45)
    if show == 999:
        print(f'\033[32m{" Volte sempre ":=^45}\033[m')
        break
    elif show > len(jogadores) - 1:
        print(f'    Jogador não cadastrado com o código {show}')
    if show < len(jogadores):
        print(f'Levantamento do jogador {jogadores[show]["Nome"]}:')
        for i, v in enumerate(jogadores[show]['Gols']):
            print(f'    No jogo {i + 1} fez {v} gols')
