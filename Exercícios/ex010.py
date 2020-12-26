print('{:$^60}'.format(' CÂMBIO DO DIA: US$1.00 = R$3.27 '))
dinheiro = float(input('Quanto reais tem? R$'))
print('Com R${:.2f} pode comprar US${:.2f}'.format(dinheiro, dinheiro/3.27))
