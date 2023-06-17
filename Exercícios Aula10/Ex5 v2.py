import random   #importa o módulo random que permite gerar valores aleatórios

#É criada a função gera_cadeia_adn que irá receber o valor da variável comprimento (será o valor do comprimento da cadeia de AND)
def gera_cadeia_adn(comprimento):
    #Cria a lista nucleotideos que contém os valores dos nucleótidos
    nucleotideos = ['A', 'C', 'G', 'T']
    #A lista cadeia_adn irá receber os valores gerados pelo módulo random, que irá ler valores à lista nucleotideos e que irá gerar valores durante a execução do ciclo for
    #que irá ser executado até ser atingido o valor definido anteriormente
    cadeia_adn = [random.choice(nucleotideos) for num in range(comprimento)]
    #retorna a lista cadeia_adn
    return cadeia_adn

#É criada a função gerador_complemento que irá receber como valor a lista cadeia_adn
def gerador_complemento(cadeia_adn):
    #complemento é um dicionário em que cada entrada corresponde ao valor do complemento DNA
    complemento = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
    #É utilizada compreensão de listas para criar uma nova lista, que irá receber os seus valores do dicionário complemento, utilizando um ciclo for para percorrer a lista cadeia_adn
    sequencia_complemento = [complemento[nucleotideo] for nucleotideo in cadeia_adn]
    #Retorna uma nova lista, que irá ser o resultado da concatenação dos elementos da lista sequencia_complemento
    return ''.join(sequencia_complemento)

#Cria uma função que servirá para definir o tamanho da cadeia de ADN que irá ser gerada
def obter_comprimento_adn():
    #O loop while é executaro até que seja retornado um valor
    while True:
        #É feita a avaliação do input inserido pelo utilizador
        try:
            comprimento = int(input("Introduza o comprimento da cadeia de DNA: "))
            #Se o número introduzido for menor ou igual a 0 é apresentada uma menssagem de erro
            if comprimento <= 0:
                print("O comprimento deve ser um número positivo. Tente novamente.")
            #Se o valor introduzido cumprir os requisitios será retornado para a variável comprimento
            else:
                return comprimento
        #Se o valor introduzido não for um número será apresentada uma mensagem de erro
        except ValueError:
            print("Valor inválido. Introduza um número inteiro positivo.")

#A variável comprimento_adn recebe o resultado da função obter_comprimento_adn
comprimento_adn = obter_comprimento_adn()
#A variável cadeia_adn recebe o resultado da função gera_cadeia_adn que foi executada chamando a variável comprimento_adn
cadeia_adn = gera_cadeia_adn(comprimento_adn)
#A variável RNA recebe o resultado da função gerador_complemento que foi executada chamando a variável cadeia_adn
RNA = gerador_complemento(cadeia_adn)

#Mostra no ecrã a contactenação da lista cadeia_adn
print("Cadeia DNA:", ''.join(cadeia_adn))
#Mostra no ecrã o resultado da lista RNA
print("Cadeia RNA:", RNA)