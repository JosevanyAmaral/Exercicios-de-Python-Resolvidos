multidao = list()
dados = list()
pesos = list()
mais_Pesadas = list()
menos_Pesadas = list()
while True:
    dados.append(str(input('Nome: ')).strip().title())
    dados.append(float(input('Peso: ')))
    pesos.append(dados[1])
    multidao.append(dados[:])
    dados.clear()
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while resp[0] not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    print('-=' * 20)
    if resp[0] in 'N':
        break
print(f'Foram cadastradas {len(multidao)} pessoas.')
for p in multidao:
    if max(pesos) == p[1]:
        mais_Pesadas.append(p[0])
    elif min(pesos) == p[1]:
        menos_Pesadas.append(p[0])
print(f'O maior peso digitado foi {max(pesos):.1f}Kg. Peso de {mais_Pesadas}.')
print(f'O menor peso digitado foi {min(pesos):.1f}Kg. Peso de {menos_Pesadas}.')
