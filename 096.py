def area(comp, larg):
    total = comp * larg
    print(f'A área de um terreno {comp} X {larg} é {total:.2f}m²')


print(f'{"Controle de Terrenos":^30}')
print('-' * 30)
largura = float(input('LARGURA (M): '))
comprimento = float(input('COMPRIMENTO (M): '))
area(comprimento, largura)
