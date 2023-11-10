numeros = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
    elif n % 2 == 1:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()

print(f'Os números pares são: {numeros[0]}')
print(f'Os números ímpares são: {numeros[1]}')
