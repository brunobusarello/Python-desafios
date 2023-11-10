valores = []
valpar = []
valimpar = []
while True:
    valores.append(int(input('Digite um  valor: ')))
    continuar = str(input('Quer continuar? '))
    if continuar in 'Nn':
        break
for i, v in enumerate(valores):
    if valores[i] % 2 == 0:
        valpar.append(v)
    elif valores[i] % 2 == 1:
        valimpar.append(v)
print(valores)
valpar.sort()
print(valpar)
valimpar.sort()
print(valimpar)
