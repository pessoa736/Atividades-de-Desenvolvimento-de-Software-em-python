import random

numeros = []

for i in range(0, 8):
    numeros.append(random.randrange(2, 90))

print("numeros")
print(numeros)

numerosQuadrados = []
for i in numeros:
    numerosQuadrados.append(i*i)

print("numero ao quadrado")
print(numerosQuadrados)