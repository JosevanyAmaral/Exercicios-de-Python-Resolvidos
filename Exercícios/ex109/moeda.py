def moeda(preco=0.0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def aumentar(preco=0, percentagem=0, formatar=False):
    resp = preco + (preco * percentagem / 100)
    return resp if not formatar else moeda(resp)


def diminuir(preco=0, percentagem=0, formatar=False):
    resp = preco - (preco*percentagem/100)
    return moeda(resp) if formatar else resp


def dobro(preco=0, formatar=False):
    resp = preco * 2
    return moeda(resp) if formatar else resp


def metade(preco=0, formatar=False):
    resp = preco / 2
    return resp if not formatar else moeda(resp)
