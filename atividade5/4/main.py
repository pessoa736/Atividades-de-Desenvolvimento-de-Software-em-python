def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return "Magro"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 40:
        return "Obeso"
    else:
        return "Obeso Mórbido"
    

print(calcular_imc(75, 1.85))