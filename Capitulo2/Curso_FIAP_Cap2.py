numero = int(input("Digite um numero de 1 a 15: "))
if numero < 1 or numero > 15:
    print('O número digitado está fora do escopo proposto!')
else:
    while numero < 20:
        print('\n\t' + str(numero))     # o \n indica "nova linha" e o \t indica uma tabulação
        numero = numero + 2
print("Laço encerrado....")
