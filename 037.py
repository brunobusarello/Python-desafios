from time import sleep
nd = int(input('\033[36mDigite um valor: \033[m'))

print('\033[7mPara operar o valor em BINÁRIO, digite 1')
print('Para operar o valor em OCTAL, digite 2')
print('Para operar o valor em HEXADECIMAL, digite 3')
print('\033[m')
sleep(3)

base = str(input('Em qual base quer operar? ')).strip().lower()

if base == '1':
    print(bin(nd)[2:])
elif base == '2':
    print(oct(nd)[2:])
elif base == '3':
    print(hex(nd)[2:])
else:
    print('Não possuo esse formato de conversão')
