listanum = []
mai = men = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print(f'Você digitou os valores: {listanum}')
print(f'O menor valor lido foi {men} e está na posição: ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i}... ', end='')
print()
print(f'O maior valor lido foi o {mai} e está na posição: ', end='')
for contador, valor in enumerate(listanum):
    if valor == mai:
        print(f'{contador}... ', end='')
