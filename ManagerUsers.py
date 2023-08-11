usuarios ={}

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

def inserir():
    login = input("Informe o login do usuário: ").upper()
    usuarios[login]=[input("Informe o nome do usuário: ").upper(), 
                         input("Informe a data dúltimo acesso: "), 
                         input("Informe a estação de trabalho do usuário: ")]

def pesquisar():
    chaveBusca = input("Informe o login a ser pesquisado: ").upper()
    lista = usuarios.get(chaveBusca)
    if lista != None:
        print("Dados pesquisados: " )
        print("Nome.............: " + lista[0])
        print("Ultimo acesso....: " + lista[1])
        print("Última estação...: " + lista[2])

def listar():
    for chave, valor in usuarios.items():
        print("Listagem de usuários: ")
        print("Login: ", chave)
        print("Dados: ", valor)

def excluir(dicionario, chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
        print("Objeto eliminado")


opcao = menu()

while opcao != "N":
    if opcao == "I":
        inserir()
    elif opcao == "P":
        pesquisar()
    elif opcao == "L":
        listar()
    elif opcao == "E":
        chave = input("Informe login a ser excluido: ").upper()
        excluir(usuarios, chave)

    opcao = menu()
