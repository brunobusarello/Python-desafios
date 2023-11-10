altura = float(input('Qual a altura da sua parede? '))
largura = float(input('Qual a largura da sua parede? '))
area = altura * largura
tinta = area / 2
print('Sua parede com dimensões de {:.2f}X{:.2f}, tendo como área total {:.2f}, precisará de {:.2f} litros de tinta para ser pintada'.format(altura, largura, area, tinta))
