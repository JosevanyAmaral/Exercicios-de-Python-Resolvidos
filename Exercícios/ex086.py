ele_matriz = list()
n = list()
for lin in range(0, 3):
    for col in range(0, 3):
        n.append(int(input(f'Digite um valor para [{lin}, {col}]: ')))
    ele_matriz.append(n[:])
    n.clear()
for lin in range(0, 3):
    for col in range(0, 3):
        print(f'[{ele_matriz[lin][col]:^5}]', end='')
    print()
