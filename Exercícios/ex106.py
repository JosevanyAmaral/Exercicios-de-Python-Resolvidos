from time import sleep


def topo(msg):
    print('\033[m\033[1;30;42m~'*len(msg))
    print(msg)
    print('~'*len(msg))
    sleep(2)


def manual(msg):
    print('\033[m\033[1;30;44m~' * len(msg))
    print(msg)
    print('~' * len(msg))
    sleep(1)
    print('\033[m\033[7;30m')
    help(opc)
    sleep(1)


def baixo(msg):
    print('\033[m\033[1;30;41m~' * len(msg))
    print(msg)
    print('~' * len(msg))


while True:
    topo('  SISTEMA DE AJUDA PyHELP  ')
    opc = str(input('\033[mFunção ou Biblioteca > ')).lower().strip()
    if opc == 'fim':
        baixo('  ATÉ LOGO  ')
        break
    manual(f"  Acessando o manual do comando '{opc}' ")
