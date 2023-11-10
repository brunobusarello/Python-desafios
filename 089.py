lista = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2:'))
    media = (nota2 + nota1) / 2
    lista.append([nome, [nota1, nota2], media])
    continuar = str(input('Quer continuar? [S/N] '))
    if continuar in 'Nn':
        break
print('-=' * 45)
print(f'{"Nº":<4}{"NOME":<15}{"MÉDIA":>8}')
print('-' * 30)
for i, v in enumerate(lista):
    print(f'{i:<4}{v[0]:<15}{v[2]:>8.2f}')
print('-' * 30)
while True:
    show = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if show == 999:
        break
    if show <= len(lista) - 1:
        print(f'Notas de {lista[show][0]} são {lista[show][1]}')
    else:
        print('Aluno não cadastrado')
    print('-' * 30)

print('programa encerrado!')
