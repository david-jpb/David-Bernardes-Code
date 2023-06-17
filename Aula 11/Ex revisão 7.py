# Façam um programa que receba um número digitado pelo utilizador e calcule a soma de todos os números de 1 até ao número digitado.
# Por exemplo, se o utilizador digitou o número 4, o output deve ser 10 (1+2+3+4=10)

valor = int(input("Digite um número: "))
total = (lambda n: sum(range(1, n + 1)))(valor)
print("A soma dos números de 1 até", valor, "é:", total)