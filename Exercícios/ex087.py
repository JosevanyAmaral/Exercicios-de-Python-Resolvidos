ele_matriz = list()
n = list()
somapar = somacol3 = maiorlin2 = 0
for lin in range(0, 3):
    for col in range(0, 3):
        n.append(int(input(f'Digite um valor para [{lin}, {col}]: ')))
        if n[col] % 2 == 0:
            somapar += n[col]
        if col == 2:
            somacol3 += n[col]
        if lin == 1 and n[col] >= maiorlin2:
            maiorlin2 = n[col]
    ele_matriz.append(n[:])
    n.clear()
print('-='*25)
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[{ele_matriz[lin][col]:^5}]', end='')
    print()
print('-='*25)
print(f'A soma de todos os valores pares vale {somapar}.')
print(f'A soma dos valores da terceira coluna vale {somacol3}.')
print(f'O maior valor da segunda linha é o número {maiorlin2}.')
