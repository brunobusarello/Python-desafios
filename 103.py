def ficha(nome, gols):
    if not nome:
        nome = 'Desconhecido'
    if not gols or gols.isascii():
        gols = 0
    return f'O jogador {nome} fez {gols} gol(s) no campeonato'


print('-' * 30)
print(ficha(nome=str(input('Nome do jogador: ')), gols=str(input('Número de gols: '))))
