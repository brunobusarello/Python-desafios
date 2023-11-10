salario = float(input('Qual é o seu salário atual? R$'))
novo = salario + (salario * 15 / 100)
print('O salário de {:.2f} reais, com 15% de aumento passará a ser {:.2f} reais'.format(salario, novo))
