'''
 Desenvolver um programa que apresente a série de Fibonacci até o décimo quinto termo. A série de Fibonacci é
formada pela sequência 1,1,2,3,5,8,13,21,34, ... etc. Ela se caracteriza pela soma de um termo posterior com seu
anterior subsequente.
'''

termoa = 1
termob = 1
cont = 0

print("Série de Fibonacci até o décimo quinto termo:")
print(termoa)  # Imprime o primeiro termo

while cont < 14:
    print(termob)
    proximo_termo = termoa + termob
    termoa = termob
    termob = proximo_termo
    cont += 1