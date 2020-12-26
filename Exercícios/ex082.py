listanum = list()
listapar = list()
listaimpar = list()
while True:
    listanum.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
for v in listanum:
    if v % 2 == 0:
        listapar.append(v)
    else:
        listaimpar.append(v)
print('-='*30)
print(f'A Lista completa é {listanum}', sep=',')
print(f'A Lista de pares é {listapar}')
print(f'A Lista de ímpares é {listaimpar}')
