from ex115.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        arq = open(nome, 'wt+')
        arq.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for c in a:
            indice = c.index(';')
            n = c[:indice].replace('\n', '')
            idade = c[indice + 1:].replace('\n', '')
            print(f'{n:<35}{idade:>3} anos')
    finally:
        a.close()


def novoCadastro(nome, idade, arq):
    try:
        a = open(arq, 'at')
    except:
        print('Erro ao abrir o arquivo! ')
    else:
        try:
            a.write(f'{nome};{idade} \n')
        except:
            print('Houve um erro na gravação do Cadastro')
        else:
            print(f'Novo registro de {nome} adicionado!')
        a.close()
