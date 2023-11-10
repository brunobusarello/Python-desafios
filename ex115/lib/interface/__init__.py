def leiaInt(valor):
    while True:
        try:
            v = int(input(valor))
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar nenhum valor\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um valor inteiro válido\033[m')
            continue
        else:
            return v


def linha(tam=45):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(f'{txt:^{len(linha())}}')
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for i, c in enumerate(lista):
        print(f'\033[33m{i + 1}\033[m - \033[36m{c}\033[m')
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc
