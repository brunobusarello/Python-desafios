def metade(n=0, sit=False):
    v = n / 2
    if sit:
        return moeda(v)
    else:
        return v


def dobro(n=0, sit=False):
    v = n * 2
    if sit:
        return moeda(v)
    else:
        return v


def aumentar(n=0, quant=0, sit=False):
    v = (quant / 100 * n) + n
    if sit:
        return moeda(v)
    else:
        return v


def diminuir(n=0, quant=0, sit=False):
    v = n - (quant / 100 * n)
    if sit:
        return moeda(v)
    else:
        return v


def moeda(v=0, m='R$'):
    return f'{m}{v:.2f}'.replace('.', ',')
