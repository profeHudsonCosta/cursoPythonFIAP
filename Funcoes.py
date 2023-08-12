def menu():
    opcao = input("O que deseja realizar? \n" + "<I> - Para inserir um usuário \n"
              +
              "<P> - Para Pesquisar um usuário \n"
              +
              "<E> - Para excluir um usuário \n"
              +
              "<L> - Para Listas um usuário \n"
              + 
              "<N> - Sair do sistema. \n"
              ).upper()
    return opcao

def inserir(dicionario):
    login = input("Informe o login do usuário: ").upper()
    dicionario[login]=[input("Informe o nome do usuário: ").upper(), 
                         input("Informe a data dúltimo acesso: "), 
                         input("Informe a estação de trabalho do usuário: ")]

def pesquisar(dicionario):
    chaveBusca = input("Informe o login a ser pesquisado: ").upper()
    lista = dicionario.get(chaveBusca)
    if lista != None:
        print("Dados pesquisados: " )
        print("Nome.............: " + lista[0])
        print("Ultimo acesso....: " + lista[1])
        print("Última estação...: " + lista[2])

def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Listagem de usuários: ")
        print("Login: ", chave)
        print("Dados: ", valor)

def excluir(dicionario, chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
        print("Objeto eliminado")
