from random import randrange 


saldo = randrange(1000, 9000, 500)

print("-----------------------------------")
print("bem vindo ao Banco Burro do Shrek")
print("-----------------------------------")

while True:
    print("digite 1 para sacar")
    print("digite 2 para depositar")
    print("digite 3 para consultar o saldo")
    print("digite 4 para sair")

    n = int(input("\n"))

    print("-----------------------------------")
    if n == 1:
        print("digite o valor a ser sacado:")
        saldo -= int(input())
    elif n == 2: 
        print("digite o valor a ser depositado:")
        saldo += int(input())
    elif n == 3:
        print("seu saldo é "+str(saldo))
    elif n ==4:
        print("saindo")
        break
    
    print("-----------------------------------")
    
    if n < 1 or n > 4:
        print("opção não existe, tente novamente\n\n")










