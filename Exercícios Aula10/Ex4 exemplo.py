# Crie uma função que retorne o valor da expressão: 2/3 + 3/5 + 4/7 + 5/9 + … + n/m, para um valor de n definido pelo utilizador.
# Verifique se o valor de n definido pelo usuário é positivo e, caso não seja, solicite outro valor até ser fornecido um valor positivo

#Cria a função cálculon
def calculon():
    #Pede um input numérico ao utilizador
    n = int(input("Por favor introduza um valor positivo: "))

#Se o input estiver fora dos valores definidos mostra uma mensagem de erro e pede novamente que o utilizado introduza um valor
    while n <= 0:
        print("Valor inválido, por favor escolha um valor positivo.")
        n = int(input("Por favor introduza um valor positivo: "))

#Cria a variável total e atribui-lhe o valor 0
    total = 0
#Executa um ciclo for cujo range é entre 0 e o valor a seguir ao definido pelo utilizador
    for contagem in range(1, n + 1):
        #A variável valor fracao executa o cálculo o resultado de cada fracao, como o primeiro valor que utilizamos para o nosso cálculo corresponde a 2/3
        #O valor do numerador seria 1+1=2 e o valor do denominador seria 2*1+1=3
        valorfracao = (contagem + 1) / (2 * contagem + 1)
        #É somado o valor da variável valorfracao à função total
        total += valorfracao
    #Retorna a variável total
    return total

#A variável resultado recebe o return da função calculon()
resultado = calculon()
#É mostrado no ecrâ o resultado da nossa expressão
print(f"O valor da expressão é: {resultado}")