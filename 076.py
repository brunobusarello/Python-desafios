lista = ('Processador', 950.10, 'Placa-mãe', 846.95, 'Placa de vídeo', 1659.99, 'Memória RAM', 389.98, 'SSD', 287.65)
print('-' * 31)
print(f'{"LISTA DE PREÇOS":^31}')
print('-' * 31)
for c in range(0, len(lista), 2):
    print(f'{lista[c]:.<20}', end='')
    print(' R$ ', end='')
    print(f'{lista[c + 1]:>7}')
print('-' * 31)
