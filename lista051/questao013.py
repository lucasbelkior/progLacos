'''
 Desenvolver um programa que imprima a tabuada de 3 a 6.
'''

numero = 3

while numero <= 6:
    print(f"Tabuada do {numero}:")
    multiplicador = 1

    while multiplicador <= 10:
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")
        multiplicador += 1
    numero += 1
