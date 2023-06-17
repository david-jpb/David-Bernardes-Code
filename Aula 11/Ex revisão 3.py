#Inicialize uma lista de 20 números inteiros. Usando compreensão de listas, armazene os números pares n numa lista PAR e os números ímpares numa lista ÍMPAR.
# Imprima ambas as listas
import random
valores =  random.sample(range(1, 200), 20)                                                                           #É utilizada uma lista com 20 valores inteiros
par, impar = ([x for x in valores if x % 2 == 0] , [x for x in valores if x % 2 != 0])                                  #Utilizando a compreensão de listas, é associado à lista par os numeros da lista "valores" que

print("Valores gerados:\t\t\t\t\t", valores)                                                                                                                        # correspondam a números pares, e à lista impar os números que correspondam aos valores impares
print("Números pares da lista valores:\t\t", par)                                                                       #É impressa a lista com os valores ímpares
print("Números ímpares da lista valores:\t", impar)