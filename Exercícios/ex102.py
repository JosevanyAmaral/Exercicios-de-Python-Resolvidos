def fatorial(n=1, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor fatorial de um número
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c} x'if c != 1 else f'{c} =', end=' ')
        f *= c
    return f


print('-' * 25)
print(fatorial(2, show=True))
