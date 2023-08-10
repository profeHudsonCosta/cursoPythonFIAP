def preencherInventario(lista):
    resp = "S"

    while resp == "S":
        equipamento = [input("Equipamento: ").upper(),
                       float(input("Valor: ")),
                       int(input("Número serial: ")),
                       input("Departamento: ").upper()
                       ]
        lista.append(equipamento)
        resp = input("Digite \"S\" para continuar: ").upper()

def exibirInventario(lista):
    for elemento in lista:
        print("Nome.........: ", elemento[0])
        print("Valor........: ", elemento[1])
        print("Serial.......: ", elemento[2])
        print("Departamento.: ", elemento[3])

def localizarPorNome(nome, lista):
    for elemento in lista:
        if nome == elemento[0]:
             print("Valor..: ", elemento[1])
             print("Serial.: ", elemento[2])

def depreciarPorNome(nome, lista, perc):
    for elemento in lista:
        if nome == elemento[0]:
             print("Valor antigo: ", elemento[1])
             elemento[1] = elemento[1]*perc
             print("Novo valor: ", elemento[1])

def excluirPorSerial(numserial, lista):
    for elemento in lista:
        if elemento[2] == numserial:
             lista.remove(elemento)

def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])

    if len(valores)>0:
        print("O equipamento mais cara custa: ", max(valores))
        print("O equipamento mais barato custa: ", min(valores))
        print("O total de equipamentos é de: ", sum(valores))

inventario = []

preencherInventario(inventario)
exibirInventario(inventario)

nomeItem = input("Informe o equipamento que deseja localizar: ").upper()

localizarPorNome(nomeItem, inventario)

nomeItem = input("Informe o equipamento que deseja depreciarar: ").upper()

tax = float(input("Informe a taxa de depreciação do equipamento: "))

depreciarPorNome(nomeItem, inventario, tax)

serialNum = int(input("Informe o número de série que deseja excluir: "))

excluirPorSerial(serialNum, inventario)

exibirInventario(inventario)

resumirValores(inventario)
