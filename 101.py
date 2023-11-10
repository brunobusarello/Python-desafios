def voto(ano):
    from datetime import date
    ano = date.today().year
    idade = ano - n
    if idade >= 65 or 18 > idade >= 16:
        return f'Com {idade} anos: VOTO OPCIONAL'
    elif idade >= 16:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    else:
        return f'Com {idade} anos: NÃO VOTA'


print('-' * 30)
n = int(input('Em que ano você nasceu? '))
print(voto(n))
