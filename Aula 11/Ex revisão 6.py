# Escreva um programa que mostre todos os números entre 5 e 100 e que são divisíveis por 7, mas não múltiplos de 5.
# Os números obtidos devem ser impressos em sequência.

valores= [x for x in range(5,101) if x % 7 == 0 and x % 5 !=0]

print(valores)