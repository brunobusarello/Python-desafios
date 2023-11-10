matriz = [[], [], []]
for c1 in range(0, 3):
    n1 = int(input(f'Digite um valor para [0, {c1}]: '))
    matriz[0].append(n1)
for c2 in range(0, 3):
    n2 = int(input(f'Digite um valor para [1, {c2}]: '))
    matriz[1].append(n2)
for c3 in range(0, 3):
    n3 = int(input(f'Digite um valor para [1, {c3}]: '))
    matriz[1].append(n3)
print('-=' * 30)

for i1, v1 in enumerate(matriz[0]):
    print(f'[ {v1} ]', end='')
    if i1 == 2:
        print()
for i2, v2 in enumerate(matriz[1]):
    print(f'[ {v2} ]', end='')
    if i2 == 2:
        print()
for i3, v3 in enumerate(matriz[2]):
    print(f'[ {v3} ]', end='')
    if i3 == 2:
        print()
