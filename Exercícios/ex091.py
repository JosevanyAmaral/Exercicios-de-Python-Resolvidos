from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6),
             'Jogador 3': randint(1, 6), 'Jogador 4': randint(1, 6)}
ranking = list()
print('Valores sorteados: ')
for c, j in jogadores.items():
    print(f'   O {c} tirou {j} no dado.')
    sleep(1)
print(f'{" RANKING DOS JOGADORES ":=^30}')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)
