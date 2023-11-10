frase = str(input('Digite uma frase: ')).upper().strip()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]
print(inverso)
if inverso == junto:
    print('É um palindromo')
else:
    print('Não é um palindromo')
