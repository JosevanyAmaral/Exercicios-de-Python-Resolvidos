from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print("""\033[1;30mSuas opções:\033[m\033[1;36m
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA\033[m""")
jogador = int(input('\033[1;30mQual é a sua jogada?\033[m '))
if jogador != 0 and jogador != 1 and jogador != 2:
    print('\033[1;31mJogada Inválida! Tente Novamente.\033[m')
    exit()
print('\033[1;36mPEDRA')
sleep(0.7)
print('PAPEL')
sleep(0.7)
print('TESOURA\033[m')
print('\033[1;30m-=\033[m'*20)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('\033[1;30m-=\033[m'*20)
if computador == 0 and jogador == 2 or computador == 1 and jogador == 0 or computador == 2 and jogador == 1:
    print('\033[1;31mCOMPUTADOR VENCE\033[m')
elif computador == jogador:
    print('\033[1;33mEMPATE\033[m')
else:
    print('\033[1;32mJOGADOR VENCE\033[m')
