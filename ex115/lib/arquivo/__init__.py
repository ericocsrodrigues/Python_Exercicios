from ex115.lib.interface import *


def arquivoExiste(nome):  # Função para verificar se o arquivo existe
    try:  # Função interna do Python para tratamentos de erro que vai tentar fazer algo
        a = open(nome, 'rt')  # Open tenta abrir o arquivo com o parâmteros 'rt' que é reed(r) e text(t)
        a.close()  # Fecha o arquvio
    except FileNotFoundError:  # Função interna do Python para tratamentos de erro que vai fazer algo caso aconteça erro
        return False
    else:
        return True


def criarArquivo(nome):  # Função para criar um arquivo .txt
    try:
        a = open(nome, 'wt+')  # Abre um arquivo de texto para escrever nele. 'wt+' write text o + cria caso não exista
        a.close()
    except:
        print('Houve um error na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO ao ler arquivo!')
    else:
        cabeçalho('CADASTRO DE USUÁRIOS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='DESCONHECIDO', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO ao escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
