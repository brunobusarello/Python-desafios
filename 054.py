from datetime import date
ano = date.today().year
cont1 = 0
cont2 = 0
for c in range(0, 7):
    nascimento = int(input('Em que ano a {}° pessoa nasceu? ').format(c))
    idade = ano - nascimento
    if idade >= 21:
        cont1 += 1
    else:
        cont2 += 1
print('\n{} das pessoas já atingiram a maioridade'.format(cont1))
print('{} das pessoas irão atingir a maioridade'.format(cont2))
