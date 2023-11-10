def leiaInt(valor):
    global n
    while True:
        n = input(valor)
        if n.isnumeric():
            return n
        else:
            print('\033[31mERRO! Digite um valor inteiro\033[m')


n = leiaInt('Digite um número: ').strip()
print(f'Você acabou de digitar o número {n}')
