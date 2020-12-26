from time import sleep
dados = list()
aux = list()
while True:
    print('-' * 30)
    aux.append(str(input('Nome: ')).title())
    aux.append(float(input('Nota 1: ')))
    aux.append(float(input('Nota 2: ')))
    aux.append((aux[1] + aux[2]) / 2)
    dados.append(aux[:])
    aux.clear()
    resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while resp[0] not in 'S/N':
        resp = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if resp in 'N':
        print('-='*25)
        break
print(f'{"No.":<4} {"NOME":<10} {"MÉDIA":>8}')
print('-' * 25)
for c in range(0, len(dados)):
    sleep(1)
    print(f"{c:<4} {dados[c][0]:<10} {dados[c][3]:>8.1f}")
while True:
    print('-' * 30)
    resp2 = int(input('Quer mostrar as notas de qual aluno? (999 interrompe): '))
    if resp2 == 999:
        print('FINALIZANDO...')
        sleep(1)
        print('<<< VOLTE SEMPRE >>>')
        break
    print(f'As notas de {dados[resp2][0]} são [{dados[resp2][1]}, {dados[resp2][2]}]')
