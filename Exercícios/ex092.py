from datetime import date
trabalhador = {'Nome': str(input('Nome: ').title().strip()),
               'Idade': date.today().year - int(input('Ano de Nascimento: ')),
               'CTPS': int(input('Carteira de Trabalho (0 não tem): '))}
if trabalhador['CTPS'] != 0:
    trabalhador['Contratação'] = int(input('Ano de contratação: '))
    trabalhador['Salário'] = float(input('Salário: R$ '))
    trabalhador['Aposentadoria'] = trabalhador['Contratação'] - (date.today().year - trabalhador['Idade']) + 35
print('-='*30)
for c, v in trabalhador.items():
    print(f'  - {c} tem o valor {v}')
