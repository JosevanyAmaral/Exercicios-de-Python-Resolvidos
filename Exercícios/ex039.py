from datetime import date
ano = int(input('Em que ano você nasceu? '))
idade = date.today().year - ano
if idade < 18:
    print('\033[1;30mVocê tem {} anos e faltam {} anos para se alistar ao serviço militar'.format(idade, 18-idade))
    print('O seu alistamento será em {}'.format(date.today().year + (18 - idade)))
elif idade == 18:
    print('\033[1;30mVocê tem {} anos e está a hora de se alistar'.format(idade))
else:
    print('\033[1;30mVocê tem {} anos e já passa {} ano(s) do tempo do seu alistamento'.format(idade, idade-18))
    print('O seu alistamento foi em {}'.format(date.today().year - (idade-18)))
