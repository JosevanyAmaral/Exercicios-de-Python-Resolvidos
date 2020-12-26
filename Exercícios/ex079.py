valores = []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso')
    else:
        print('Valor duplicado! Não vou adicionar.')
    resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resposta[0] not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if resposta[0] in 'N':
        break
print('-='*30)
valores.sort()
print(f'Valores digitados ordenados: {valores}')
