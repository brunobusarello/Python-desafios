from time import sleep


def maior(* num):
    m = 0
    print('\033[36m-=\033[m' * 30)
    print('Analisando os valores passados...')
    if len(num) > 0:
        for i, n in enumerate(num):
            print(n, end=' ')
            sleep(0.4)
            if i == 0:
                m = n
            else:
                if n > m:
                    m = n
        print()
    print(f'Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {m}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
