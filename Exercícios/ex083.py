exp = str(input('Digite uma expressão: '))
"""pilha = []
for simb in exp:
    if simb in '(':
        pilha.append('(')
    elif simb in ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) > 0:
    print('A sua expressão está inválida')
else:
    print('A sua expressão está válida')"""
if exp.count('(') == exp.count(')'):
    print('A sua expressão está válida')
else:
    print('A sua expressão está inválida')
