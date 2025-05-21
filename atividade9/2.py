
def inverter_palavras(frase):
    return ' '.join(frase.split()[::-1])


if __name__ == "__main__":
    frase = "Python é incrível"
    print(inverter_palavras(frase))