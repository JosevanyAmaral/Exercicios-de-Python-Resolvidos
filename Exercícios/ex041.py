from datetime import date
ano_Nascimento = int(input('Digite o ano de nascimento do Atleta: '))
idade = date.today().year - ano_Nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('\033[1;31mClassificação: MIRIM\033[m')
elif idade <= 14:
    print('\033[1;32mClassificação: INFANTIL\033[m')
elif idade <= 19:
    print('\033[1;33mClassificação: JÚNIOR\033[m')
elif idade <= 25:
    print('\033[1;34mClassificação: SÊNIOR\033[m')
else:
    print('\033[1;35mClassificação: MASTER\033[m')
