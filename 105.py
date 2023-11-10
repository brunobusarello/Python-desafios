def notas(* n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param n: Recebe as notas do aluno (podendo ser quantas preferir)
    :param sit: Valor booleano opcional para mostrar a situação do aluno
    :return: Dicionário com informações dos dados coletados
    """
    mai = men = med = 0
    r = {}
    r['Total'] = len(n)
    for i, c in enumerate(n):
        med += c
        if i == 0:
            men = mai = c
        else:
            if c > mai:
                mai = c
            if c < men:
                men = c
    r['Maior'] = mai
    r['Menor'] = men
    r['Média'] = med / len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r


# Programa Principal
resp = notas(5.5, 9.5, 10, 6.5, sit=True)
print(resp)
