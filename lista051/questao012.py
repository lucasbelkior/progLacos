'''
 Desenvolver um programa que peça ao usuário para digitar diversos números reais, e ao final, exibir o maior e o
menor número que foram digitados, além da média entre TODOS os números digitados pelo usuário. A inserção
de números deve parar quando o usuário digitar o número -1, e este número -1 não deve ser considerado nem
como maior, nem como menor, e nem na contagem da média
'''


maior_numero = float('-inf')
menor_numero = float('inf')
soma_numeros = 0
contador_numeros = 0


numero = float(input("Digite um número real (ou -1 para encerrar): ")

while numero != -1:

    if numero > maior_numero:
        maior_numero = numero
    if numero < menor_numero:
        menor_numero = numero

    
    soma_numeros += numero
    contador_numeros += 1


    numero = float(input("Digite outro número real (ou -1 para encerrar): "))


if contador_numeros > 0:

    media = soma_numeros / contador_numeros


    print(f"O maior número digitado (excluindo -1) é: {maior_numero}")
    print(f"O menor número digitado (excluindo -1) é: {menor_numero}")
    print(f"A média dos números digitados (excluindo -1) é: {media}")
else:
    print("Nenhum número (excluindo -1) foi inserido.")
