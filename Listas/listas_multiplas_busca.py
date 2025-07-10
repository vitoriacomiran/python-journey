equipamento = []
valores = []
serial = []
departamento = []
resposta = "S"

while resposta == "S":
    equipamento.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    serial.append(int(input("Serial: ")))
    departamento.append(input("Departamento: "))
    resposta = input("Deseja continuar? [S/N]: ").upper()

busca=input("\nDigite o nome do equipamento que deseja buscar: ")
for indice in range(0, len(equipamento)):
    if busca==equipamento[indice]:
        print("Valor: ", valores[indice])
        print("Serial: ", serial[indice])
