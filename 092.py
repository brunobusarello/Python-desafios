from datetime import date
ano = date.today().year
dados = {}
dados['Nome'] = str(input('Nome: '))
dados['Idade'] = ano - int(input('Ano de nascimento: '))
dados['CTPS'] = int(input('CTPS (0 se não tiver): '))
if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: R$ '))
    dados['Aposentadoria'] = dados['Idade'] - ano + dados['Contratação'] + 35
print('\033[36m-=\033[m' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')
