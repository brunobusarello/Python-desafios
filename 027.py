nome = str(input('Digite o seu nome completo: ')).title().strip()
n = nome.split()
print('Seu primeiro nome é: {}'.format(n[0]))
print('O seu último nome é: {}'.format(n[len(n) - 1]))
