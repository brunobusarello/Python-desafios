nota1 = float(input('Digite sua 1° nota: '))
nota2 = float(input('Digite sua 2° nota: '))

media = (nota1 + nota2) / 2

if media > 10:
    print('Você não pode obter uma média maior que 10')
elif 10 >= media >= 7:
    print('Parabéns, sua média foi {:.2f} e você está aprovado'.format(media))
elif 7 > media >= 5:
    print('Sua média foi {:.2f} e você está de recuperação!'.format(media))
else:
    print('Estude mais!! Você está reprovado, pois sua média foi {:.2f}'.format(media))
