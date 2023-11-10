from datetime import date

ano = date.today().year
nasc = int(input('Em que ano você nasceu? '))
idade = ano - nasc

if idade == 18:
    print('Já está na hora de você se alistar em {}!'.format(ano))
elif idade > 18:
    tempo = idade - 18
    print('\033[31mJá passou da hora de se alistar!\033[m \033[34mVocê se alistou?\033[m')
    print('Se você não se alistou, você está \033[31m{} anos atrasado em {}!\033[m'.format(tempo, ano))
    print('Deveria ter se alistado em {}'.format(nasc + 18))
else:
    tempo = 18 - idade
    print('\033[32mVocê ainda irá se alistar, pequeno jovem!\033[m')
    print('Faltam \033[34m{}\033[m anos para o seu alistamento em {}'.format(tempo, ano))
    print('Seu alistamento será em {}'.format(nasc + 18))
