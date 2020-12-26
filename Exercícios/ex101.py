def voto(an):
    from datetime import date
    idade = date.today().year - an
    print(f'Com {idade} anos:', end=' ')
    if idade < 16:
        return 'VOTO NEGADO.'
    elif 18 <= idade <= 65:
        return 'VOTO OBRIGATÓRIO.'
    else:
        return 'VOTO OPCIONAL.'


print('-'*25)
nasc = int(input('Ano de Nascimento: '))
print(voto(nasc))
