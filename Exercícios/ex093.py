dados = {'nome': str(input('Nome do Jogador: ').strip().title()),}
golos = list()
tot_partidas = int(input(f"Quantas partidas {dados['nome']} jogou? "))
for c in range(0, tot_partidas):
    golos.append(int(input(f'Quantos golos na {c+1}ª partida? ')))
dados['golos'] = golos[:]
dados['total'] = sum(golos[:])
print('-='*40)
print(dados)
print('-='*40)
for c, v in dados.items():
    print(f'O campo {c} tem o valor {v}.')
print('-='*40)
print(f"O jogador {dados['nome']} jogou {tot_partidas} partidas.")
for p, v in enumerate(golos):
    print(f'   => Na partida {p+1}, fez {v} golos.')
print(f'Foi um de total de {dados["total"]} golos.')
