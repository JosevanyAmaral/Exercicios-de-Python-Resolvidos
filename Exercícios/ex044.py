print('{:^60}'.format('\033[1;33mJOALHARIA AMARAL\033[m'))
pagamento = float(input('Preço das compras: R$'))
print("""\033[1;30mFORMAS DE PAGAMENTO
[ 1 ] À vista dinheiro/cheque
[ 2 ] À vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão\033[m""")
opcao = int(input('Qual é a sua opção de de pagamento? '))
if opcao == 1:
    print('\033[1;32mO total a ser pago são R${:.2f} com 10% de desconto'.format(pagamento-pagamento*0.1))
elif opcao == 2:
    print('O total a ser pago são R${:.2f} com 5% de desconto'.format(pagamento-pagamento*0.05))
elif opcao == 3:
    print('O total a ser pago são R${:.2f} sem desconto'.format(pagamento))
elif opcao == 4:
    print('O total a ser pago são R${:.2f} já incluídos os 20% de juros = {:.0f}\033[m'.
          format(pagamento+pagamento*0.2, pagamento*0.2))
else:
    print('\033[1;31mOpção inválida! Por favor tente novamente.\033[m')
