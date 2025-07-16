# um equipamento com determinado número serial foi danificado e será descartado.
# é necessário eliminar ele.
# para eliminar usar o comando 'del'

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


descartar = int(input("Digite o serial do equipamento que será descartado: "))
for indice in range(0, len(departamentos)):
      if seriais == seriais[indice]:
          del departamentos[indice]
          del seriais[indice]
          del valores[indice]
          break
for indice in range(0,len(equipamentos)):
    print("Equipamento: ", (indice+1))
    print("Nome: ", equipamentos[indice])
    print("Valor: ", valores[indice])
    print("Serial: ", seriais[indice])
    print("Departamento: ", departamentos[indice])

