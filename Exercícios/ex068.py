from random import randint
from time import sleep
vitorias = 0
print('{:-^60}\n'.format(' JOGO DO PAR OU ÍMPAR '))
while True:
    print('-=' * 60)
    computador = randint(1, 10)
    jogador = int(input('Diga um valor: '))
    soma = jogador + computador
    parouimpar = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    while parouimpar[0] not in 'PI':
        parouimpar = str(input('Oops! Tente outra vez. Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print('-' * 60)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} ', end='')
    print('deu PAR'if soma % 2 == 0 else 'deu ÍMPAR')
    print('-' * 60)
    sleep(1)
    if parouimpar[0] in 'I':
        if soma % 2 == 0:
            print('Você \033[1;31mPERDEU!')
            break
        else:
            vitorias += 1
            print('Você \033[1;32mVENCEU\033[m')
    else:
        if soma % 2 == 1:
            print('Você \033[1;31mPERDEU!')
            break
        else:
            vitorias += 1
            print('Você \033[1;32mVENCEU\033[m')
    print('Vamos jogar novamente...')
print(f'Game Over! Você venceu {vitorias} vez'if vitorias == 1 else f'Game Over! Você venceu {vitorias} vezes')
