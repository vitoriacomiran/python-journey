#converter uma variável em outra
name = "Vitória"
age = 28
price = 5.5
is_student = True

print(type(name))
#retorna o tipo da variável, nesse caso str para transformar uma variável em outra

price = int(price)

print(price)

#vai retornar apenas 5

age = float(age)

print(age)

#vai retornar 28.0

#se transformar um int em uma string, o número passa a ser reconhecido como texto e não como numeral, logo se fizer isso:

age = str(age) # o valor de 28 deixa de ser int e vira str ou seja, texto

age += 1 # se a variável age fosse um int retornaria 29 (28+1)

#como a variável age virou str o resultado é 251