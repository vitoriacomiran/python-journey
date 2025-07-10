equipamento = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamento.append(input("equipamento: "))
    valores.append(float(input("valor: ")))
    seriais.append(int(input("seriais: ")))
    departamentos.append(input("departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()

for indice in range (0, len(equipamento)):
    print("\nequipamento: ", (indice + 1))
    print("nome: ", equipamento[indice])
    print("valor: ", valores[indice])
    print("serial: ", seriais[indice])
    print("departamento: ", departamentos[indice])

# indice => identificador do elemento da lista
# irá mostrar cada item da lista
# como a lista pode ter infinitas entradas, inicia no 0
# len(equipamento) retorna o número de itens na lista equipamentos

# ou seja:
# para cada número começando do 0 até o número de itens na lista equipamento (sem incluir esse último número)
# pegue esse número e chame de indice