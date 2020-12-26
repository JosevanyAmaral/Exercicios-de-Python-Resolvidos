def leiaint(txt):
    while True:
        try:
            num = int(input(txt))
        except (TypeError, ValueError):
            print('\033[1;31mERRO: Por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31mO Usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num


def leiafloat(txt):
    while True:
        try:
            num = float(input(txt))
        except (TypeError, ValueError):
            print('\033[1;31mERRO: Por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;31mO Usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return num


n1 = leiaint('Digite um  número Inteiro: ')
n2 = leiafloat('Digite um número Real:')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')
