from ex107 import moeda
p = float(input('Digite o preço: R$'))
print(f'A metade de {p:.2f} é {moeda.metade(p):.2f}')
print(f'O dobro de {p:.2f} é {moeda.dobro(p):.2f}')
print(f'Aumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p, 13)}')
