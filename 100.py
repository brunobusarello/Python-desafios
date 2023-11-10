from random import randint
from time import sleep
lista = []


def sorteia(quant):

    """
    Sorteador de números aleatórips (podendo se repetir) de 1 até 10
    :param quant: Informa quantos números serão sorteados
    :return: Sem retorno
    OBS.: Os valores serão armazenados em uma lista
    """
    lista.clear()
    print(f'Sorteando {quant} valores da lista: ', end='')
    for c in range(0, quant):
        n = randint(1, 10)
        print(n, end=' ')
        sleep(0.18)
        lista.append(n)
    print('PRONTO!')


def somapar(num):
    par = 0
    for n in num:
        if n % 2 == 0:
            par += n
    print(f'Somando os valores pares de {lista}, temos {par}')


sorteia(5)
somapar(lista)

help(sorteia)
