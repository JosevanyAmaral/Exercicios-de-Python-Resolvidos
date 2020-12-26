from random import randint
n_aleatorios = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
menor = maior = cont = 0
for c in n_aleatorios:
    print(c, end=' ')
print(f'\nO maior valor sorteado foi: {max(n_aleatorios)}')
print(f'O menor valor sorteado foi: {min(n_aleatorios)}')
