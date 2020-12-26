termo = int(input('\033[1;30mDigite o primeiro termo da P.A:'))
razao = int(input('Digite o valor da razão:'))
print('Os 10 primeiros termos dessa P.A são:\033[m')
for c in range(1, 11):
    print('\033[1;35m{},'.format(termo+(c-1)*razao), end='')
print('...\033[m')
