#Crie um programa em Python que conte quantas vezes cada nome está presente numa lista ['nome1', 'nome2,...] e armazene ess contagem num dicionário
#{'nome1: xvezes, nome2: xvezes}
from collections import Counter
lista=['Emma', 'Liam', 'Olivia', 'Noah', 'Ava', 'Isabella', 'Sophia', 'Jackson', 'Mia', 'Aiden', 'Lucas', 'Luna', 'Oliver', 'Amelia', 'Charlotte', 'Harper', 'Elijah', 'Emily', 'Henry', 'Evelyn', 'Michael', 'Alexander', 'James', 'Benjamin', 'Daniel', 'Matthew', 'William', 'Joseph', 'Scarlett', 'Gabriel', 'Samuel', 'David', 'Victoria', 'Andrew', 'Chloe', 'Abigail', 'Elizabeth', 'Mason', 'Ella', 'Sofia', 'Ethan', 'Lily', 'Aria', 'Grace', 'Logan', 'Camila', 'Penelope', 'Ryan', 'Nora', 'Noah', 'Luna', 'Gabriel', 'Daniel', 'Chloe']

ocorrencias = Counter(lista)

print(ocorrencias)