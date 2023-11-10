def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: O número a ser calculado
    :param show: É opcional. Para mostrar ou não a conta
    :return: O valor do Fatorial de um número
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(f'{c} {"X" if c != 1 else "="} ', end='')
    return f


print(fatorial(5))
