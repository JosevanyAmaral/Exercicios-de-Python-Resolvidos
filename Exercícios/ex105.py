def notas(* n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    print('-'*30)
    dados = {'total': len(n), 'maior': max(n), 'menor': min(n), 'média': sum(n)/len(n)}
    if sit:
        if dados['média'] < 5:
            dados['situação'] = 'RUIM'
        elif dados['média'] >= 7:
            dados['situação'] = 'BOA'
        else:
            dados['situação'] = 'RAZOÁVEL'
    return dados


resp = notas(3.5, 2, 6.5, sit=True)
print(resp)
