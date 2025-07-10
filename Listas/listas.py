#lista para quando precisa de múltiplas entradas de variáveis

inventario=[] #lista
resposta="S"

# a função do append é inserir o dado dentro da lista
while resposta=="S":
    inventario.append(input("Informe o equipamento: "))
    inventario.append(float(input("Informe o valor: ")))
    inventario.append(int(input("Informe o número de serie: ")))
    inventario.append(input("Departamento: "))

    resposta=input("Digite \"S ou N\" para continuar? ").upper()
# o \ é para o sistema não interpretar as aspas como parte do código
# o upper é para validar o S, o sistema entender que pode ser tanto minúsculo quanto maiúsculo


# ele ficará rodando esse código sempre, enquanto o while não for interrompido
# ou seja, enquanto a resposta for S irá continuar

for elemento in inventario:
    print(elemento)

# quando eu digitar o N, acaba o loop, logo irá aparecer a lista gerada