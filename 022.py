nome = str(input('Digite o seu nome completo: '))
nome = nome.strip()
print('Formatação do nome: \n\n{}'.format(nome.upper()))
print('{} \n '.format(nome.lower()))
nospc = nome.replace(' ', '')
print('Seu nome completo tem {} caracteres.'.format(len(nospc)))

div = nome.split()
print('Seu primeiro nome tem {} caracteres.'.format(len(div[0])))
