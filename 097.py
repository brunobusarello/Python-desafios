def escreva(phs):
    tam = len(phs) + 4
    print('\033[36m~\033[m' * tam)
    print(f'{phs:^{tam}}')
    print('\033[36m~\033[m' * tam)


escreva('Bruno Gustavo Busarello')
escreva('Gustavo Guanabara')
escreva('1')
