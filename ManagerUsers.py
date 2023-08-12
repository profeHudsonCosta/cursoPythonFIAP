usuarios ={}

from Funcoes import*

usuarios ={}

opcao = menu()

while opcao != "N":
    if opcao == "I":
        inserir(usuarios)
    elif opcao == "P":
        pesquisar(usuarios)
    elif opcao == "L":
        listar(usuarios)
    elif opcao == "E":
        chave = input("Informe login a ser excluido: ").upper()
        excluir(usuarios, chave)

    opcao = menu()
