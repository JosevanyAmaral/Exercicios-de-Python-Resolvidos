aluno = dict()
aluno['Nome'] = str(input('Nome: ')).strip().title()
aluno['Media'] = float(input(f"Média de {aluno['Nome']}: "))
print('-='*30)
if aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'
for c, v in aluno.items():
    print(f'  - {c} é igual a {v}.')