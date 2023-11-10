n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

lista = [n1, n2, n3]
if n1 == max(lista):
    print('{} é o maior número'.format(n1))
if n2 == max(lista):
    print('{} é o maior número'.format(n2))
if n3 == max(lista):
    print('{} é o maior número'.format(n3))
if n1 == min(lista):
    print('{} é o menor número'.format(n1))
elif n2 == min(lista):
    print('{} é o menor número'.format(n2))
elif n3 == min(lista):
    print('{} é o menor número'.format(n3))
