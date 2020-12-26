dados = dict()
pessoas = list()
m = 0
while True:
    dados.clear()
    dados['nome'] = str(input('Nome: ').strip().title())
    while True:
        dados['sexo'] = str(input('Sexo: [M/F] ').upper().strip()[0])
        if dados['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    m += dados['idade']
    resp = str(input('Quer continuar? [S/N]').upper().strip()[0])
    while resp[0] not in 'SN':
        print('ERRO! Responda apenas S ou N')
        resp = str(input('Quer continuar? [S/N]').upper().strip()[0])
    if resp[0] in 'N':
        break
print('-='*40)
m /= len(pessoas)
print(f'- O grupo tem {len(pessoas)} pessoas.')
print(f'- A média de idade é de {m:.2f} anos.')
print(f'- As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] in 'F':
        print(p['nome'], end=', ')
print('\nLista das pessoas que estão acima da média:')
for p in pessoas:
    if p['idade'] > m:
        for c, v in p.items():
            print(f'{c} = {v};', end=' ')
print('\n<< ENCERRADO >>')
