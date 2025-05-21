
def remover_duplicatas(lista):
    return list(dict.fromkeys(lista))


if __name__ == "__main__":
    
    numeros = [1, 2, 2, 3, 4, 4, 5]
    print(remover_duplicatas(numeros)) 