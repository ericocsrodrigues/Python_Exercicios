from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cadastro_usuarios.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        cabeçalho('\033[34mOpção - 1\033[m')
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('\033[34mOpção - 2\033[m')
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('\033[31mSaindo do sistema >>> Até logo!2\033[m')
        break
    else:
        cabeçalho('\033[41mERRO! Digite uma opção válida!\033[m')
    sleep(2)
