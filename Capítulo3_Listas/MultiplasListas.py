equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite 'S' para continuar: ").upper()

for indice in range(0, len(equipamentos)):
    print("Equipamento..: ", (indice+1))
    print("Nome.........: ", equipamentos[indice])
    print("Valor........: ", valores[indice])
    print("Serial.......: ", seriais[indice])
    print("Departamento.: ", departamentos[indice])

busca = input("Digite o nome do equipamento que deseja buscar: ")
for indice in range(0, len(equipamentos)):
    if busca == equipamentos[indice]:
        print("Valor..: ", valores[indice])
        print("Serial.:", seriais[indice])

depreciacao = input('Informe o nome do equipamento que será depreciado: ')
for indice in range(0, len(equipamentos)):
    if depreciacao == equipamentos[indice]:
        valores[indice] = valores[indice] * 0.9
        print(f'O equipamento {equipamentos[indice]} foi depreciado em 10%')
        print('O novo valor é: ', valores[indice])

serial = int(input('Digite o serial do equipamento que será excluído: '))
for indice in range(0, len(departamentos)):
    if seriais[indice] == serial:
        del departamentos[indice]
        del equipamentos[indice]
        del seriais[indice]
        del valores[indice]
        break

for indice in range(0, len(equipamentos)):
    print('Equipamento..: ', (indice+1))
    print('Nome.........: ', equipamentos[indice])
    print('Valor........: ', valores[indice])
    print('Serial.......: ', seriais[indice])
    print('Departamento.: ', departamentos[indice])
