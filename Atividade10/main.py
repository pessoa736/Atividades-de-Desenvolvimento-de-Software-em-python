import matplotlib.pyplot as mtp

def verificarSeENumero(valor):
        try:
            if "." in valor or "," in valor:
                valor = valor.replace(",", ".")
                return float(valor)
            return int(valor)
        except ValueError:
            return valor 


def grafico(arquivo, coluna_x=0, coluna_y=1, separador=";", titulo="Gráfico", xlabel="Eixo X", ylabel="Eixo Y", nome_arquivo="grafico.png"):
    with open(arquivo, encoding="utf-8") as f:
        dados = f.readlines()

    x = []
    y = []

    for i in range(1, len(dados)):
        linha = dados[i].strip().split(separador)
        x.append(verificarSeENumero(linha[coluna_x]))
        y.append(verificarSeENumero(linha[coluna_y]))
    
    
    mtp.plot(x, y, marker='o', linestyle='-', color='b')

    mtp.xlabel(xlabel)
    mtp.ylabel(ylabel)
    mtp.title(titulo)
    mtp.grid(True)
    mtp.savefig(nome_arquivo, dpi=300)
    mtp.close()

grafico(
    "populacao_brasileira.csv", 
    0, 1, ";", 
    "População Brasileira ao Longo dos Anos", 
    "ano", "população", 
    "popuBrasLongAno.png"
)
grafico(
    "vendas_mes.csv", 
    0, 1, ";", 
    "vendas por mes", 
    "vendas", "mes", 
    "vendMes.png"
)