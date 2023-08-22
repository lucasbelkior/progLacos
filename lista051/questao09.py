'''
 Elaborar um programa que apresente no final a soma dos valores pares existentes na faixa de 0 até 500. Utilize
um laço que efetue a variação de 2 em 2
'''

contador = 1
acumulador = 0

while ( contador <= 500 ):
    div = contador % 2
    if (div == 0):
        print(f"{contador}")
    acumulador = acumulador + contador
    contador = contador + 1

print("A soma dos valores de 0 a 500 é igual", acumulador)
