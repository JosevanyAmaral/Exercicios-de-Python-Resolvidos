from random import randint
from time import sleep
print('-=-' * 20)
print('Pensei em um número entre 0 e 5...')
print('-=-' * 20)
n = randint(0, 5)
escolha = int(input('Adivinhe em que número eu pensei:'))
print('PROCESSANDO...')
sleep(3)
print('PARABÉNS! VOCÊ ACERTOU!' if n == escolha else 'OOPS! VOCÊ ERROU!\nEU PENSEI NO NÚMERO {}'.format(n))
