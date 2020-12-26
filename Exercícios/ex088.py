from random import randint
from time import sleep
numeros_sorteados = list()
aux = list()
print('-'*40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-'*40)
jogos = int(input('Quantos jogos quer sortear? '))
for cont_Palpites in range(0, jogos):
    for cont_Sorteados in range(0, 6):
        num = randint(1, 60)
        while num in aux:
            num = randint(1, 60)
        aux.append(num)
    aux.sort()
    numeros_sorteados.append(aux[:])
    aux.clear()
print(f'{" SORTEANDO {} JOGOS ":=^40}'.format(jogos))
for c in range(0, jogos):
    print(f'Jogo {c+1}: {numeros_sorteados[c]}')
    sleep(1)
print('{:-^40}'.format(' < BOA SORTE! > '))
