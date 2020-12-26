n = int(input('Que tabuada quer visualizar? '))
for c in range(1, 11):
    print('{} X {:2} = {}'.format(n, c, n*c))
