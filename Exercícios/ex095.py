dados = {}
jogadores = []
golos = list()
while True:
    dados.clear()
    print('-'*35)
    dados['nome'] = str(input('Nome: ')).strip().title()
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for c in range(0, partidas):
        golos.append(int(input(f'Quantos golos marcou na {c+1}ª partida? ')))
    dados['golos'] = golos[:]
    dados['total'] = sum(golos[:])
    jogadores.append(dados.copy())
    golos.clear()
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp[0] in 'SN':
            break
        print("ERRO! Digite apenas 'S' ou 'N'.")
    if resp[0] in 'N':
        break
print('-='*30)
print('cod ', end='')
for i in dados.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(jogadores):
    print(f'{k:<3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    opc = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if opc == 999:
        break
    if opc > len(jogadores):
        print(f'ERRO! Não existe jogador com código {opc}!')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[opc]["nome"].upper()}')
        for j, g in enumerate(jogadores[opc]['golos']):
            print(f'  No jogo {j+1} fez {g} golos')
    print('-' * 40)
print('<< VOLTE SEMPRE >>')
