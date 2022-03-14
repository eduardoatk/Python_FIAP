def perguntar():
    resposta = input("O que deseja realizar?" +
            "\n\t<I> - Para Inserir um usuário" +
            "\n\t<P> - Para Pesquisar um usuário" +
            "\n\t<E> - Para Excluir um usuário" +
            "\n\t<L> - Para Listar um usuário: ").upper()
    return resposta

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
            input("Digite a última data de acesso: "),
            input("Qual a última estação acessada: ").upper()]

def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista != None:
        print('\nNome..................:' + lista[0])
        print('Data último acesso....:' + lista[1])
        print('Hora último acesso....:' + lista[2] + '\n')

def excluir(dicionario, chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
    print('Usuário de login', chave, ' excluído!')

def listar(dicionario):
    for chave, valor in dicionario.items():
        print('\n========================\n')
        print('Login: ', chave)
        print('Dados: ', valor)
        print('\n========================\n')
