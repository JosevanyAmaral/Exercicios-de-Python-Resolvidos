numeros = []
while True:
    numeros.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while resp[0] not in 'SN':
        resp = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
    if resp[0] in 'N':
        break
numeros.sort(reverse=True)
print('-='*30)
print(f'Foram digitados {len(numeros)} números')
print(f'Lista ordenada de forma decrescente: {numeros}')
print('O número 5 está na lista'if 5 in numeros else'O número 5 não está na lista')
