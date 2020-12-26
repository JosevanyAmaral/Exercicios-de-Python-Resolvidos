from time import sleep
from emoji import emojize
print('Contagem regressiva o ano novo!')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emojize('\033[1;30mFELIZ ANO NOVOOOOOOOOOOO!:boom::fireworks:', use_aliases=True))
