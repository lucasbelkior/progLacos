'''
 Elaborar um programa que apresente o valor de uma potência de uma base qualquer (Variável b) elevada a um
expoente qualquer (Variável e), ou seja, de be
. (Sem usar Math.pow();)
'''

b = float(input("Informe a base da potencia:"))
e = float(input("Informe o expoente da potencia:"))

contador = 1
acumulador = 1
while (contador <= e):
    acumulador = acumulador * b
    contador = contador + 1

print(f"{b:.0f} elevado a {e:.0f} = {acumulador:.0f}")