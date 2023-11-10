numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezesete', 'dezoito', 'dezenovo', 'vinte')
while True:
    n = int(input('Digite um número entre 1 e 20: '))
    if n < 1 or n > 20:
        print('Tente novamente. ', end='')
    else:
        print(f'Você digitou o número {numeros[n]}')
        break
