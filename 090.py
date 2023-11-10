boletim = {}
boletim['Nome'] = str(input('Nome: '))
boletim['Média'] = float(input(f'Média de {boletim["Nome"]}: '))
if boletim['Média'] >= 7:
    boletim['Situação'] = 'Aprovado'
elif 5 <= boletim['Média'] < 7:
    boletim['Situação'] = 'Recuperação'
else:
    boletim['Situação'] = 'Reprovado'

for k, v in boletim.items():
    print(f'{k} é igual a {v}')
