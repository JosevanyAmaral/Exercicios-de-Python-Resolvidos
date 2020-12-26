def contador():
    from time import sleep
    print('-='*20)
    print('Contagem de 1 até 10 de 1 em 1')
    for c in range(1, 11):
        sleep(0.3)
        print(c, end=' ')
    print('FIM!')
    print('-=' * 20)
    print('Contagem de 10 até 0 de 2 em 2')
    for c in range(10, -1, -2):
        sleep(0.3)
        print(c, end=' ')
    print('FIM!')
    print('-=' * 20)
    print('Agora é a sua vez de personalizar a contagem!')
    i = int(input('Início: '))
    f = int(input('Fim: '))
    n = p = int(input('Passo: '))
    print('-=' * 20)
    if n < 0 or i < 0 and p < 0:
        n *= -1
        p = n
    elif n == 0:
        n = -1
    print(f'Contagem de {i} até {f} de {n} em {n}')
    if i > f:
        f -= 1
        if p > 0:
            p = -p
        elif p == 0:
            p = -1
    else:
        f += 1
    for c in range(i, f, p):
        sleep(0.3)
        print(c, end=' ')
    print('FIM!')


contador()
