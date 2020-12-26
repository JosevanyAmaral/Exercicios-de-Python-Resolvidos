valores = posmai = posmen = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {cont}: ')))
for pos, v in enumerate(valores):
    if v == 0:
        posmai = posmen = v
    else:
        if v == max(valores):
            posmai.append(pos)
        elif v == min(valores):
            posmen.append(pos)
print('-=' * 30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} na posições {posmai}')
print(f'O menor valor digitado foi {min(valores)} nas posições {posmen}')
