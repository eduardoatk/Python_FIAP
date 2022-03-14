# Para que seja apresentada a porta do Arduíno ele deve estar conectado
# caso contrário irá retornar a mensagem de que não há portas disponíveis

import serial

conexao = ""
for porta in range(10):
    try:
        conexao = serial.Serial("COM"+str(porta), 115200, timeout=0.5)
        print("Conectado na porta: ", conexao.portstr)
        break
    except serial.SerialException:
        pass
if conexao != "":
    conexao.close()
    print("Conexão encerrada")
else:
    print("Sem portas disponíveis")
