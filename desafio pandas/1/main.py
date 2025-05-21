import pandas as pd
import criar_planilha as cp


cp.criar_planilha('vendas.xlsx') 

df = pd.read_excel('vendas.xlsx') # Carregar os dados da planilha

df['Total'] = df['Quantidade'] * df['Preço Unitário']
df['Data'] = pd.to_datetime(df['Data'])
df['AnoMes'] = df['Data'].dt.to_period('M')

vendas_mensais = df.groupby('AnoMes')['Total'].sum().reset_index()
mes_maior_faturamento = vendas_mensais.loc[vendas_mensais['Total'].idxmax()]

# Salvar o resultado em uma nova planilha
vendas_mensais.to_excel('vendas_mensais.xlsx', index=False)