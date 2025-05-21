
def trocar_primeira_ultima(palavras):
    if len(palavras) < 2:
        return palavras
    palavras[0], palavras[-1] = palavras[-1], palavras[0]
    return palavras

if __name__ == "__main__":
    
    palavras = ["azul", "verde", "amarelo", "vermelho"]
    print(trocar_primeira_ultima(palavras))