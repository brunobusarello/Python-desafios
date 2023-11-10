cores = {'branco': '\033[7m', 'amarelo': '\033[43m', 'azul': '\033[44m', 'vermelho': '\033[41m'}
from time import sleep


def estilo(texto, linha=False, cor=''):
    print('\033[m', end='')
    print(cores[cor], end='')
    if linha:
        tam = len(texto) + 4
        print('-' * tam)
        print(f'{texto:^{tam}}')
        print('-' * tam)
    else:
        print(texto)


while True:
    estilo('Sistema de Ajuda PyHelp', True, 'amarelo')
    v = str(input('\033[mFunção ou biblioteca > '))
    sleep(0.3)
    if v == 'fim':
        estilo('ATÉ LOGO', True, 'vermelho')
        break
    estilo(f"Acessando o manual do comando '{v}'", True, 'azul')
    sleep(1)
    estilo(v.__doc__, False, 'branco')
    sleep(4)
