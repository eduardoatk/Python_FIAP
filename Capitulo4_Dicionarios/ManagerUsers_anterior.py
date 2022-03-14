usuarios = {}
opcao = input("O que deseja realizar?" +
            "\n\t<I> - Para Inserir um usuário" +
            "\n\t<P> - Para Pesquisar um usuário" +
            "\n\t<E> - Para Excluir um usuário" +
            "\n\t<L> - Para Listar um usuário: ").upper()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        chave = input("Digite o login: ").upper()
        usuarios[chave] = [input("Digite o nome: ").upper(),
                           input("Digite a última data de acesso: "),
                           input("Qual a última estação acessada: ").upper()]
    opcao = input("O que deseja realizar?" +
                  "<I> - Para Inserir um usuário" +
                  "<P> - Para Pesquisar um usuário" +
                  "<E> - Para Excluir um usuário" +
                  "<L> - Para Listar um usuário: ").upper()
