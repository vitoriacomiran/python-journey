nome=input("Digite seu nome: ")
idade=int(input("Digite sua idade: "))
doenca=input("Suspeita de doença: ").upper()

if idade>=65:
    print(f"O paciente {nome} de {idade} anos possui atendimento prioritário")
elif doenca=="SIM":
    print(f"O paciente {nome} tem urgencia no atendimento")
else:
    print(f"O paciente {nome} de {idade} anos não possui atendimento prioritário")
