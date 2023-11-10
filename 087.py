matriz = [[], [], []]
pares = []
resultadopar = 0
resultadocol3 = []
col3 = 0
coluna3 = []
maior = menor = 0
for c1 in range(0, 3):
    n1 = int(input(f'Digite um valor para [0, {c1}]: '))
    matriz[0].append(n1)
    if n1 % 2 == 0:
        pares.append(n1)
    if c1 == 2:
        resultadocol3.append(n1)
for c2 in range(0, 3):
    n2 = int(input(f'Digite um valor para [1, {c2}]: '))
    matriz[1].append(n2)
    if n2 % 2 == 0:
        pares.append(n2)
    if c2 == 0:
        maior = menor = n2
    else:
        if n2 > maior:
            maior = n2
        if n2 < menor:
            menor = n2
    if c2 == 2:
        resultadocol3.append(n2)
for c3 in range(0, 3):
    n3 = int(input(f'Digite um valor para [2, {c3}]: '))
    matriz[1].append(n3)
    if n3 % 2 == 0:
        pares.append(n3)
    if c3 == 2:
        resultadocol3.append(n3)
print('-=' * 30)

for i1, v1 in enumerate(matriz[0]):
    print(f'[ {v1} ]', end='')
    if i1 == 2:
        print('\n')
for i2, v2 in enumerate(matriz[1]):
    print(f'[ {v2} ]', end='')
    if i2 == 2:
        print('\n')
for i3, v3 in enumerate(matriz[2]):
    print(f'[ {v3} ]', end='')
    if i3 == 2:
        print('\n')
print('\n')
print('-=' * 30)
for c in pares:
    resultadopar += c
print(f'A soma dos números pares é {resultadopar}')
for v in resultadocol3:
    col3 += v
print(f'A soma dos valores da 3° coluna é {col3}')
print(f'O maior valor da 2° linha é {maior}')
