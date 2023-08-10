equipamentos = []
valores = []
seriais = []
departamentos = []

resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: ").upper())
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite S para continuar: ").upper()

for indice in range(0, len(equipamentos)):
    print("Equipamento..: ", (indice+1))
    print("Nome.........: ", equipamentos[indice])
    print("Valor........: ", valores[indice])
    print("Serial.......: ", seriais[indice])
    print("Departamento.: ", departamentos[indice])

deprec = 0

for indice in range(0, len(equipamentos)):
    if equipamentos[indice] == "IMPRESSORA":
        deprec = valores[indice] * 0.1
        valores[indice] = valores[indice] - deprec

busca = input("Digite o nome do equipamento que deseja buscar: ").upper()

for indice in range(0,len(equipamentos)):
    if busca ==equipamentos[indice]:
        print("Valor..: ", valores[indice])
        print("Serial.:", seriais[indice])

buscaSerial = int(input("Informe o número de série do equipamento: "))

for indice in range(0, len(seriais)):
    if buscaSerial == seriais[indice]:
        del equipamentos[indice]
        del valores[indice]
        del seriais[indice]


for indice in range(0, len(equipamentos)):
    print("Equipamento..: ", (indice+1))
    print("Nome.........: ", equipamentos[indice])
    print("Valor........: ", valores[indice])
    print("Serial.......: ", seriais[indice])
    print("Departamento.: ", departamentos[indice])
