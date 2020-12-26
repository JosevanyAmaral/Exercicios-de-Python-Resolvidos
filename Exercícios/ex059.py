from time import sleep
escolha = 0
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite mais um valor:'))
while escolha != 5:
    print("""      PRESSIONE:
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA\n""")
    escolha = int(input('Escolha uma opção: '))
    if escolha == 5:
        print('Saindo do Programa...')
        sleep(3)
    else:
        if escolha == 1:
            print('A soma entre {} e {} vale {}\n'.format(n1, n2, n1 + n2))
        elif escolha == 2:
            print('O produto de {} X {} vale {}\n'.format(n1, n2, n1 * n2))
        elif escolha == 3:
            print('{} é maior do que {}\n'.format(n1, n2)if n1 > n2 else '{} é maior do que {}\n'.format(n2, n1))
        elif escolha == 4:
            print('Insira os novos números:\n')
            n1 = int(input('Digite um valor: '))
            n2 = int(input('Digite mais um valor:'))
        else:
            print('Opção Inválida. Volte a Tentar.\n')
