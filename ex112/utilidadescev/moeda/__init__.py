def metade(n, sit=False):
    r = n / 2
    if sit:
        return moeda(r)
    else:
        return r


def dobro(n, sit=False):
    r = n * 2
    if sit:
        return moeda(r)
    else:
        return r


def aumentar(n, quant, sit=False):
    r = (quant / 100 * n) + n
    if sit:
        return moeda(r)
    else:
        return r


def diminuir(n, quant, sit=False):
    r = n - (quant / 100 * n)
    if sit:
        return moeda(r)
    else:
        return r


def moeda(v=0, m='R$'):
    return f'{m}{v:.2f}'.replace('.', ',')


def resumo(v=0, mai=10, men=5):
    tam = 30
    print('\033[36m-' * tam)
    print(f'{"RESUMO DO VALOR":^{tam}}')
    print('-' * tam)
    print(f'\033[7mPreço analisado: \t{moeda(v)}\033[m')
    print(f'Dobro do preço: \t{dobro(v, True)}')
    print(f'Metade do preço: \t{metade(v, True)}')
    print(f'{mai}% de aumento: \t{aumentar(v, mai, True)}')
    print(f'{men}% de redução: \t{diminuir(v, men, True)}')
    print('-' * tam)
