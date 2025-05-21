import pandas as pd

def criar_planilha( nome_arquivo):
    dados = {
        'Data': ['2024-01-15', '2024-01-20', '2024-02-10', '2024-02-25', '2024-03-05'],
        'Produto': ['A', 'B', 'A', 'C', 'B'],
        'Quantidade': [10, 5, 8, 12, 7],
        'Preço Unitário': [20.0, 35.0, 20.0, 15.0, 35.0]
    }
    df_exemplo = pd.DataFrame(dados)

    df_exemplo.to_excel(nome_arquivo, index=False) # Criar um arquivo Excel de exemplo