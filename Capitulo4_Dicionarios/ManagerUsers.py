from Funcoes import *

usuarios = {}
opcao = perguntar()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)
    if opcao == "P":
        pesquisar(usuarios, input('Digite o login: ').upper())
    if opcao == "E":
        excluir(usuarios, input('Digite o login do usuário que deseja excluir: ').upper())
    if opcao == "L":
        listar(usuarios)
    opcao = perguntar()
