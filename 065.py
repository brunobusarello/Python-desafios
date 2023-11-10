# Variáveis
continuar = ' '
soma = cont = maior = menor = media = 0

# While
while continuar not in 'Nn':
    num = int(input('Digite um número: '))
    continuar = str(input('Quer continuar [ S/N ]? '))
    if cont == 0:
        menor = num
        maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    soma += num
    cont += 1
    media = soma / cont

# Respostas
print('Você digitou {} número{} e a média foi {:.2f}'.format(cont, 's' if cont >= 2 else '', media))
print('O maior número é {} e o menor é {}'.format(maior, menor))

