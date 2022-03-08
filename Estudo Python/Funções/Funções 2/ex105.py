def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias).
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma
    """
    dic = dict()
    dic['total'] = len(n)
    dic['maior'] = max(n)
    dic['menor'] = min(n)
    dic['média'] = sum(n)/len(n)
    if sit == True:
        if dic['média'] < 5:
            dic['situação'] = 'RUIM'
        elif 5 <= dic['média'] <= 7:
            dic['situação'] = 'MARROMENO'
        else:
            dic['situação'] = 'TÁBAUM'
    return dic


# Programa principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
help(notas)
