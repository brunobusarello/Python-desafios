matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
        if c == 2:
            scol += matriz[l][c]
        if l == 1:
            if c == 0:
                mai = matriz[l][c]
            else:
                if matriz[l][c] > mai:
                    matriz[l][c] = mai
print('\033[36m-=\033[m' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]:^5} ]', end='')
    print()
print('\033[36m-=\033[m' * 30)
print(f'A soma dos valores pares é {spar}')
print(f'A soma dos valores da 3° coluna é {scol}')
print(f'O maior valor da 2° linha é {mai}')
