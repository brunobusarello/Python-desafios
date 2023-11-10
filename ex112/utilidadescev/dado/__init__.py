def leiaDinheiro(v):
    while True:
        n = input(v).replace(',', '.').strip()
        novo = n.replace('.', '')
        if novo.isdigit():
            break
        print(f'\033[31mERRO! "{n}" é um preço inválido!\033[m')
    return float(n)
