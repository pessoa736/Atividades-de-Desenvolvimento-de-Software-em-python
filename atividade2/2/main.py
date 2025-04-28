



def repeticao_de_letra(palavra, letra_escolhida):
    repitcao = 0
    for letra in palavra:
        if letra == letra_escolhida:
            repitcao += 1
    return repitcao

print(repeticao_de_letra("raspberry","r"))