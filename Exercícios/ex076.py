listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00,
            'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-'*50)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print('-'*50)
for cont in range(0, len(listagem), 2):
    print(f'{listagem[cont]:.<40}R$ {listagem[cont+1]:6.2f}')
print('-'*50)
