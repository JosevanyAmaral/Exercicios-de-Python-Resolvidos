val = float(input('Qual é o valor da casa? R$'))
salario = float(input('Digite o seu salário: R$'))
anos = int(input('Em quantos anos vai pagar? '))
prestacao = val / (anos*12)
print('Para pagar uma casa de R${:.2f} em {} anos a prestação mensal será de R${:.2f}'.format(val, anos, prestacao))
if salario * 0.3 < prestacao:
    print('EMPRÉSTIMO NEGADO!')
    print('O seu salário é insuficiente para completar esse empréstimo')
else:
    print('EMPRÉSTIMO CONCEDIDO!')
    print('Mensalmente lhe será descontado R${:.2f} durante {} anos'.format(prestacao, anos))
