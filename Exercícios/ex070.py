total_Gasto = maisde_1000 = mais_Barato = 0
nome_Maisbarato = ''
print('-' * 40)
print(f'{"CANTINA DO MAMADÚ":^40}')
print('-' * 40)
while True:
    nome_Produto = str(input('Nome do Produto: ')).strip().title()
    preco = float(input('Preço: R$'))
    total_Gasto += preco
    if preco > 1000:
        maisde_1000 += 1
    if mais_Barato == 0 or preco < mais_Barato:
        mais_Barato = preco
        nome_Maisbarato = nome_Produto
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('Tente novamente. Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta[0] in 'N':
        break
    print('-' * 40)
print(f'O total da compra foi R${total_Gasto:.2f}')
print(f'Temos {maisde_1000} produto custando mais de R$1000.00'if maisde_1000 == 1
      else f'Temos {maisde_1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_Maisbarato:} que custa R${mais_Barato:.2f}')
