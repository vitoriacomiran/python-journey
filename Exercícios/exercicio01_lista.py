# Todos os equipamentos 'impressora' receberão depreciação (desvalorização) de 10%
# Monte um código que seria responsável por alterar o valor de todos os equipamentos 'impressora'.
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
  resposta = input("Digite \"S\" para continuar: ").upper()

for indice in range(0,len(equipamentos)):
  print("Equipamento: ", (indice+1))
  print("Nome: ", equipamentos[indice])
  print("Valor: ", valores[indice])
  print("Serial: ", seriais[indice])
  print("Departamento: ", departamentos[indice])

depreciacao = input("Digite o nome do equipamento que será depreciado: ")
for indice in range(0,len(equipamentos)):
    if depreciacao==equipamentos[indice]:
        print("Valor antigo: ", valores[indice])
        valores[indice] = valores[indice] * 0.9
        print("Novo valor: ", valores[indice])