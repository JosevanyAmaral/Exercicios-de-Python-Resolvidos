def aumentar(preco=0, percentagem=0):
    return preco + (preco*percentagem/100)


def diminuir(preco=0, percentagem=0):
    return preco - (preco*percentagem/100)


def dobro(preco=0):
    return preco * 2


def metade(preco=0):
    return preco / 2


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
