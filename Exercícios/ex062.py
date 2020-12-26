primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite o valor da razão: '))
contador = 1
termo = primeiro
qtdtermos = 0
resposta = 10
while resposta != 0:
    qtdtermos += resposta
    while contador <= qtdtermos:
        print('{}'.format(termo), end=' → ')
        termo += razao
        contador += 1
    print('PAUSA')
    resposta = int(input('Quantos termos mais deseja visualizar? '))
print('Progressão Finalizada com {} termos'.format(qtdtermos))

""" while resposta != 0:
    contador = 1
    while contador <= resposta:
        print('{}'.format(termo), end=' → ')
        termo += razao
        qtdtermos += 1
        contador += 1
    print('PAUSA')
    resposta = int(input('Quantos termos mais deseja visualizar? '))
print('Progressão Finalizada com {} termos'.format(qtdtermos))"""
