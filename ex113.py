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

def leiaFloat(valor):
    while True:
        try:
            v = float(input(valor))
        except KeyboardInterrupt:
            print('\n\033[31mO usuário preferiu não digitar nenhum valor\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um valor real\033[m')
            continue
        else:
            return v


n = leiaInt('Digite um número: ')
n1 = leiaFloat('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro {n} e o número real {n1:.2f}')
