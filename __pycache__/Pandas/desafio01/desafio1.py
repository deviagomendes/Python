#Procure um dataset no Kaggle, remova a primeira e a última coluna do dataset, plote algum tipo de gráfico que traga informações do dataset.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('__pycache__/Pandas/desafio01/olist_sellers_dataset.csv')
remover_colunas = df.drop(df.columns[0:2], axis=1)
ordenar = remover_colunas.sort_values(by=remover_colunas.columns[1])
dfc = df.copy()
df = ordenar.rename(columns={'seller_city': 'Cidade', 'seller_state': 'Estado'})
df = df.drop_duplicates(subset=['Cidade'])

df_cidadeporestados = df.groupby('Estado')['Cidade'].count().reset_index(name='Cidades')
df = df_cidadeporestados
ordenar1 = df.sort_values(by='Cidades', ascending=False)
df = ordenar1
print(df)

#PLOTANDO O GRÁFICO EM BARRAS
plt.figure(figsize=(50, 50))
plt.bar(df['Estado'], df['Cidades'], color='blue')

plt.title('Quantidade de lojas por estado')
plt.xlabel('Estados')
plt.ylabel('Cidades')

plt.show()