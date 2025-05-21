
def ordenar_por_tamanho(lista):
    return sorted(lista, key=len)

if __name__ == "__main__":
    palavras = ["abacaxi", "maçã", "kiwi", "banana", "laranja", "uva", "manga"]
    print(ordenar_por_tamanho(palavras))