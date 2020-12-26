def moeda(preco=0.0, moeda='R$'):
    return f'{moeda:}{preco:.2f}'.replace('.', ',')


def aumentar(preco=0, percentagem=10, formatar=False):
    resp = preco + (preco*percentagem/100)
    return resp if not formatar else moeda(resp)


def diminuir(preco=0, percentagem=5, formatar=False):
    resp = preco - (preco*percentagem/100)
    return moeda(resp) if formatar else resp


def dobro(preco=0, formatar=False):
    resp = preco * 2
    return moeda(resp) if formatar else resp


def metade(preco=0, formatar=False):
    resp = preco / 2
    return resp if not formatar else moeda(resp)


def resumo(preco, aumento=10, reducao=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{aumento}% de aumento: \t{aumentar(preco, aumento, True)}')
    print(f'{reducao}% de redução: \t{diminuir(preco, reducao, True)}')
    print('-' * 30)
