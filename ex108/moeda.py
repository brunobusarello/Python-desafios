def metade(n=0):
    return n / 2


def dobro(n=0):
    return n * 2


def aumentar(n=0, quant=0):
    return (quant / 100 * n) + n


def diminuir(n=0, quant=0):
    return n - (quant / 100 * n)


def moeda(v=0, m='R$'):
    return f'{m}{v:>8.2f}'.replace('.', ',')
