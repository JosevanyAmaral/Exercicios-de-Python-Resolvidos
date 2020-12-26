n = int(input('Digite um número:'))
totdiv = 0
for c in range(1, n+1):
    if n % c == 0:
        totdiv = totdiv + 1
if totdiv == 2:
    print('O número {} é primo.'.format(n))
else:
    print('O número {} não é primo.'.format(n))
