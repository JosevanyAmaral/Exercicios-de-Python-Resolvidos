s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont += 1
print('A soma dos {} números ímpares múltiplos de 3 que estão no intervalo entre 1 e 500 foi {}'.format(cont, s))
