sexo = ' '
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual o sexo da pessoa? ')).upper()
print('Sexo {} registrado!'.format(sexo))
