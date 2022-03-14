inventario = []
resposta = 'S'

# Adicionar item no inventário
while resposta == 'S':
    equipamento = [input('Equipamento: '),
                   float(input('Valor: ')),
                   int(input('Número serial: ')),
                   input('Departamento: ')]
    inventario.append(equipamento)
    resposta = input('Digite "S" para continuar: ').upper()

# Exibir dados do inventário
for elemento in inventario:
    print('\nNome...........:', elemento[0])
    print('Valor..........:', elemento[1])
    print('Serial.........:', elemento[2])
    print('Departamento...:', elemento[3])

# Localizar um item no inventário
busca = input('Digite o nome do equipamento que deseja buscar: ')
for elemento in inventario:
    if busca == elemento[0]:
        print('Valor....: ', elemento[1])
        print('Serial...:', elemento[2])

# Depreciar um item do inventário
depreciacao = input('Digite o nome do equipamento que será depreciado: ')
for elemento in inventario:
    if depreciacao == elemento[0]:
        print('Valor antigo....: ', elemento[1])
        elemento[1] = elemento[1] * 0.9
        print('Novo valor......: ', elemento[1])

# Excluir um item do inventário
serial = int(input('Digite o número serial do equipamento que será descartado: '))
for elemento in inventario:
    if elemento[2] == serial:
        inventario.remove(elemento)

# Exibir dados do inventário
for elemento in inventario:
    print('\nNome...........:', elemento[0])
    print('Valor..........:', elemento[1])
    print('Serial.........:', elemento[2])
    print('Departamento...:', elemento[3])

# Resumo de valores do inventário
valores = []
for elemento in inventario:
    valores.append(elemento[1])
if len(valores) > 0:
    print('O equipamento mais caro custa: ', max(valores))
    print('O equipamento mais barato custa: ', min(valores))
    print('O total de equipamentos é de: ', sum(valores))
