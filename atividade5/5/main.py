def calcular_viagem(km_por_litro, distancia, preco_litro):
    litros = distancia / km_por_litro
    custo = litros * preco_litro
    return litros, custo

distancia = 20  #km
disLit = 4      #km
precoGasosa = 19.90 # a inflação.....

litros, custo = calcular_viagem(disLit, distancia, precoGasosa)

print(
    "numa viajem de " + str(distancia) + "km, no qual cada litro de gasosa dar para viajar "+ str(disLit) + 
    "km de distancia. o qual vai gastar " + str(litros) + "L de gasosa e R$" + str(custo) 
)