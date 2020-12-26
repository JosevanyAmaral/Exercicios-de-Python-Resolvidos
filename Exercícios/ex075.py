n = ((int(input('Digite o 1º valor: '))), (int(input('Digite o 2º valor: '))),
     (int(input('Digite o 3º valor: '))), (int(input('Digite o 4º valor:'))))
totdiv = 0
print(f'Você digitou ou valores {n}')
print(f'O valor 9 apareceu {n.count(9)} vez'if n.count(9) == 1 else f'O valor 9 apareceu {n.count(9)} vezes')
print(f'O valor 3 não foi digitado em nenhuma posição' if 3 not in n
      else f'O valor 3 apareceu pela 1ª vez na {n.index(3) + 1}ª posição')
print('Os valores pares digitados foram', end=' ')
for cont in n:
    if cont % 2 == 0:
        print(cont, end=' ')
