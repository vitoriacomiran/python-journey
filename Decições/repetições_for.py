tabuada=int(input("Digite um número: "))
print(f"Tabuada do número {tabuada}")

for valor in range(1,11,1): #inicio, fim e incremento (começa em 1, vai até 10, e aumenta de 1 em 1)
    print(str(tabuada) + "x" + str(valor) + "=" + str((tabuada*valor)))

