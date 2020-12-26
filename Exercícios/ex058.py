from random import randint
from emoji import emojize
from time import sleep
ntentativas = 1
print('\033[1;35m-=\033[m'*20)
print('\033[1;30mPensando em um número entre 0 e 10...')
computador = randint(0, 10)
jogador = int(input(emojize('Em que número eu pensei?\033[m:sunglasses: ', use_aliases=True)))
print('\033[1;35m-=\033[m'*20)
while jogador != computador:
    sleep(1)
    print(emojize('\033[1;31mVOCÊ ERROU! EU NÃO PENSEI NO NÚMERO {}:poop:\033[m'.format(jogador), use_aliases=True))
    jogador = int(input(emojize('\033[1;30mTente Novamente\033[m:sunglasses: ', use_aliases=True)))
    ntentativas += 1
print('\033[1;35m-=\033[m'*20)
sleep(1)
print(emojize('\033[1;30mVOCÊ ACERTOU! EU PENSEI NO NÚMERO {}:disappointed:'.format(jogador), use_aliases=True))
print('Foram precisas {} tentativas\033[m'.format(ntentativas))
