exp = str(input('Digite uma expressão numérica: ')).strip()
caracteres = []
for c in exp:
    if c == '(':
        caracteres.append('(')
    elif c == ')':
        if len(caracteres) > 0:
            caracteres.pop()
        else:
            caracteres.append(')')

if len(caracteres) == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')

