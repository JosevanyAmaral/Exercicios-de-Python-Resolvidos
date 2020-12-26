while True:
    n = int(input('Quer ver a tabuada de qual número? '))
    print('-' * 40)
    if n < 0:
        break
    for cont in range(1, 11):
        print(f'{n:2} x {cont:2} = {n*cont:2}')
    print('-' * 40)
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')
