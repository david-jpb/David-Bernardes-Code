#Escreve uma programa que receba uma string do utilizador e a mostre de trás para a frente

frase = str(input("Por favor introduza uma frase:"))

fraseinvertida = ''.join(reversed(frase))
print(fraseinvertida)