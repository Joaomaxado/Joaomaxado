import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:/Users/Maria/OneDrive/Documentos/João A/ecommerce_preparados.csv')

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
print(df.head())

# Histograma
plt.figure(figsize=(6,6))
plt.hist(df['N_Avaliações'])
plt.title('Avaliações')
plt.ylabel('Quantidade')
plt.show()

# Dispersão
plt.scatter(df['N_Avaliações'], df['N_Avaliações_MinMax'])
plt.title('Dispersão - Avaliações')
plt.xlabel('Avaliações_MinMax')
plt.ylabel('Qtd de Avaliações')
plt.show()

# Mapa de calor
corr = df[['N_Avaliações', 'Preço']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Mapa de Calor')
plt.tight_layout()
plt.show()

# Gráfico de Barra
df.dropna()
plt.figure(figsize=(6,6))
df['Temporada'].value_counts().plot(kind='bar', color='red')
plt.title('Divisão de temporadas')
plt.xlabel('Temporada')
plt.ylabel('Quantidade')
# plt.xticks(rotation=0)
plt.show()

# Gráfico de Pizza
z = df['Temporada'].value_counts()

limite = 10

z_filtrada = z[z >= limite]
outros = z[z < limite].sum()
if outros < 0:
    z['Outros'] = outros
plt.figure(figsize=(10,6))
plt.pie(z_filtrada.values, labels=z_filtrada.index, autopct = '%.1f%%', startangle = 90)
plt.title('Distribuição de temporada')
plt.show()

# Gráfico de densidade
sns.kdeplot(df['Preço'], fill=True, color='pink')
plt.title('Densidade do Preço')
plt.xlabel('Preço')
plt.show()

# Gráfico de Regressão
sns.regplot(x='N_Avaliações', y='Preço', data=df, color='brown', scatter_kws={'alpha':0.5})
plt.title('Regressão de preço e avaliações')
plt.show()