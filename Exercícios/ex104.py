def leiaInt(txt):
    print('-' * 30)
    while True:
        num = input(txt)
        if num.isnumeric():
            break
        print('\033[1;31mERRO! Digite um número inteiro válido.\033[m')
    return num


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
