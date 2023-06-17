# MAP
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# lista1 = list(map(lambda x: x**2, lista))
# print("lista = ", lista,"\n\nlista1 = ", lista1)


#Reduce
# from functools import reduce
# lista = [1, 2, 3, 4, 5, 6]
# lista = [1, 2, 3, 4, 5]
# lista = [1, 2, 3, 4]
# lista = [1, 2, 3]
# lista = [1, 2]
# produto = reduce(lambda x,y: x * y, lista)
# print("lista = ", lista,"\n\n = ", produto)


#Filter
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
#impar
lista1 = list(filter(lambda x: x % 2 != 0, lista))
#par
lista2 = list(filter(lambda x: x % 2 == 0, lista))
#múltiplos de 3
lista3 = list(filter(lambda x: x % 3 == 0, lista))
#múltiplos de 4
lista4 = list(filter(lambda x: x % 4 == 0, lista))
#múltiplos de 5
lista5 = list(filter(lambda x: x % 5 == 0, lista))
#múltiplos de 6
lista6 = list(filter(lambda x: x % 6 == 0, lista))
#múltiplos de 7
lista7 = list(filter(lambda x: x % 7 == 0, lista))
print("lista = ", lista,"\n\nNumeros Ímpares = \t", lista1)
print("Numeros Pares = \t", lista2)
print("Múltiplos de 3 = \t", lista3)
print("Múltiplos de 4 = \t", lista4)
print("Múltiplos de 5 = \t", lista5)
print("Múltiplos de 6 = \t", lista6)
print("Múltiplos de 7 = \t", lista7)