def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return n


def lin(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(lin())
    print(txt.center(42))
    print(lin())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[31m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(lin())
    opc = leiaInt('\033[31mSua opção: \033[m')
    return opc

