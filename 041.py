from datetime import date
ano = date.today().year

a = int(input('Digite sua data de nascimento: '))

idade = ano - a
print('O atleta tem {} anos'.format(idade))

if a >= ano - 9:
    print('Você é um nadador mirim')
elif a >= ano - 14:
    print('Você é um nadador infantil')
elif a >= ano - 19:
    print('Você é um nadador júnior')
elif a >= ano - 20:
    print('Você é um nadador sênior')
else:
    print('Você é um nadador master')
