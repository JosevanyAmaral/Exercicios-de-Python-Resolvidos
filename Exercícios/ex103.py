def ficha(n, qg):
    if len(n) == 0:
        n = '<desconhecido>'
    if not qg.isnumeric():
        qg = '0'
    print(f'O jogador {n} fez {qg} golo(s) no campeonato.')


print('-' * 25)
nome = str(input('Nome do Jogador: ')).title().strip()
golos = str(input('Número de golos: '))
ficha(nome, golos)
