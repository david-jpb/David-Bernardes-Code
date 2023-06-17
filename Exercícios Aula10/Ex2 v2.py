import random                   #importa o modulo random, que permite a geração de números aleatórios
from collections import Counter #importa a funcionalidade Counter, que permite realizar contagens

numero_lancamentos = 1000000        #Variável que corresponde ao número total de lançamentos
lancamentos = [random.randint(1, 6) for cont in range(numero_lancamentos)]  #cCria uma lista que será populada por um ciclo for cujo núemro de ciclos corresponde à
# variável numero_lancamentos, e que irá receber os seus valores a partir do gerador random.randint(1, 6) que irá gerar valores aleatórios entre 1 e 6.

#Frequência corresponde ao equivalente a um dicionario, que chama o objeto counter, que irá receber keys (os números 1-6) e a quantidade de vezes que cada
#número aconteceu
frequencia = Counter(lancamentos)

#Cria uma lista chamada numeros_ordenados, que irá ordenar a variável frequencia por ordem crescente mediante o valor das chaves
numeros_ordenados = sorted(frequencia.keys())

#Calcula a percentagem de vezes que cada número ocorreu e mostra os resultados
#Cria um loop for, que vai iterar todos os elementos da lista numeros_ordenados
for numero in numeros_ordenados:
    #Cria a variável contagem que chama a variável frequencia
    contagem = frequencia[numero]
    #É calculada a percentagem que equivale à quantidade de vezes que cada número ocorreu
    percentagem = contagem / numero_lancamentos * 100
    #É mostrada uma formatted string que indica o número, a quantidade de vezes que ocorreu e a percentagem respetiva
    print(f"O numero {numero} occurreu {contagem} vezes, o que equivale a uma percentagem de {percentagem:.4f}%")