numero = int(input('Digite um número inteiro:'))
escolha = str(input('\033[31m-1 para binário\033[m\n\033[32m-2 para octal\033[m\n\033[34m-3 para hexadecimal\033[m\n'))
if escolha == '1':
    print('O número \033[30m{}\033[m em decimal é \033[30m{:0b}\033[m em binário'.format(numero, int(numero)))
elif escolha == '2':
    print('O número \033[30m{}\033[m em decimal é \033[30m{:0o}\033[m em octal'.format(numero, int(numero)))
elif escolha == '3':
    print('O número \033[30m{}\033[m em decimal é \033[30m{:0x}\033[m em hexadecimal'.format(numero, int(numero)))
else:
    print('Comando Inválido!')
#bin(numero[2:])
