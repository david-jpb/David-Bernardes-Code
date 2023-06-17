#A função verificanum verifica se o numero n é um número perfeito
def verificanum(n):
    #É executado um ciclo for de 1 até ao valor introduzido e se n for igual à soma dos divisores de n que tenham resultado 0, trata-se de um número perfeito
    #Por exemplo 6%1=0 , 6%2=0, 6%3=0, 1+2+3=6
    return n == sum(i for i in range(1, n) if n % i == 0)

#A função procuranum executa um ciclo for com o range do valor após o número definido
def procuranum(n):
    #É criada uma lista de compreensão quer etorna os valores em que o valor i seja executado com sucesso pela função verificanum(i)
    return [i for i in range(1, n+1) if verificanum(i)]

#Pede ao utilizador que introduza o valor que irá ser passado à função verificanum
num = int(input("Este número é perfeito?\n "))
#Se a função for executada com sucesso é mostrada a mensagem abaixo
if verificanum(num):
    print(f"{num} é um número perfeito.")
#Se a função não foi executada com sucesso, é retornada a mensagem seguinte
else:
    print(f"{num} não é um número perfeito.")
#Pede ao utilizador que introduza até que valor deseja verificar a existência de números perfeitos
limite = int(input("Mostrar todos os números perfeitos até: "))
#A variável nums_perfeitos recebe o return da função procuranum(limite)
nums_perfeitos = procuranum(limite)
#É apresentada no ecrâ a lista dos números perfeitos existentes no intervalo indicado
print("Números Perfeitos:", nums_perfeitos)