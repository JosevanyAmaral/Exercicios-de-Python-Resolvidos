from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    nascimento = int(input('Digite o {}º ano de nascimento:'.format(c)))
    if date.today().year - nascimento < 21:
        menor += 1
    else:
        maior += 1
print('Das 7 pessoas, {} ainda não é/são maior(es) e {} já é/são maior(es)'.format(menor, maior))
