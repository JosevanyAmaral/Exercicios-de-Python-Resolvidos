def sorteia(lista):
    from random import randint
    from time import sleep
    print('Sorteando os 5 valores da lista:', end=' ')
    for c in range(0, 5):
        lista.append(randint(1, 10))
        print(lista[c], end=' ')
        sleep(0.5)
    print('PRONTO!')


def soma_par(lista):
    s = 0
    for c in range(0, len(lista)):
        if lista[c] % 2 == 0:
            s += lista[c]
    print(f'Somando os valores pares de {lista}, temos {s}')


numeros = list()
sorteia(numeros)
soma_par(numeros)
