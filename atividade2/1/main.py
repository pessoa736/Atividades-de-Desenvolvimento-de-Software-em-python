import random

tabela = []

for i in range(0, 100):
    tabela.append(random.randrange(0, 100))

print("tabela1 =")
print(tabela)

sum = sum(tabela)

print("a soma de todos elementos dessa tabela é: "+ str(sum))