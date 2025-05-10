cores = {}

def addCor(nome, codigo_hex):
    id = "cor " + str(len(cores) + 1)
    cor = {
        "nome": nome,
        "codigo_hex": codigo_hex
    }
    cores[id] = cor

def showCores():
    for c in cores:
        st = "- " + c + " \n"
        for info in cores[c]:
            st = st + "\t" + info + ": '" + str(cores[c][info]) + "'\n"
        print(st)

# Exemplo de uso:
addCor("vermelho", "#FF0000")
addCor("verde", "#00FF00")
addCor("azul", "#0000FF")
addCor("amarelo", "#FFFF00")

showCores()