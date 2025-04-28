
altura = float(input("\n\n(em metros,e nâo em quilometros) qual a sua altura?\n"))
peso = float(input("\ndiga-me seu peso\n"))


def Imc(a, p):
    return p/(a**2)

imc = Imc(altura, peso)

if imc < 18.5:
    print("abaixo do peso")
elif imc >18.5 and imc<24.9:
    print("peso normal")
elif imc > 25 and imc <29.9:
    print("acima do peso")
elif imc > 30:
    print("obeso") 

