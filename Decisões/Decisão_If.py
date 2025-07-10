nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
if idade >= 65:
    print(f"O paciente {nome} possui atendimento prioritário pois tem {idade} anos")
else:
    print(f"O paciente {nome} logo será atendido na final normal")
