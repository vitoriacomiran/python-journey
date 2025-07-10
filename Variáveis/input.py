#Função usada para receber uma informação do usuário, retorna uma string

name = input("Qual o seu nome? ")

# o usuário insere a resposta

print(f"Olá {name}")

###

#calcular a área de um retangulo

length = input("Enter the length ")
width = input("Enter the width ")

area = length * width

print(area)


#nesse caso vai dar erro, pois o input é str, não tem como multiplicar str
#precisa transformar em int ou float

length = int(input("Enter the length "))
width = int(input("Enter the width "))

area = length * width

print(area)

#ou

print(f"the area is: {area}cm²")


###

#calcular um pedido
item = input("O que você deseja comprar? ")
valor = float(input("Qual o valor? "))
quantidade = int(input("Quantos itens são? "))

total = valor * quantidade

print(f"Você comprou {quantidade} x {item}")
print(f"O valor total foi: {total}")

##
nome = input("Digite um funcionário: ")
empresa = input("Digite o nome do empresa: ")
qtd_funcionario = int(input("Quantidade de funcioários: "))
salario = float(input("Qual o valor do seu salario: "))

print (f"O nome do funcionário é {nome} e a sua empresa é {empresa} que possui {qtd_funcionario} funcionários")
print (f"{nome} ganha {salario:.3f} reais por mês")

