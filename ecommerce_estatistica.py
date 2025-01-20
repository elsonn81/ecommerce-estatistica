import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Ler o arquivo CSV
df = pd.read_csv('C:/Users/eliel/OneDrive/Área de Trabalho/Python/ecommerce_estatistica.csv')

# Configuração inicial
plt.style.use('ggplot')

# Gráfico de Histograma
plt.figure(figsize=(8, 6))
sns.histplot(df['Nota'], bins=10, kde=True, color='blue', alpha=0.7)
plt.title('Distribuição das Notas dos Produtos', fontsize=16)
plt.xlabel('Nota', fontsize=14)
plt.ylabel('Frequência', fontsize=14)
plt.show()

# Gráfico de Dispersão
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df['Preço'], y=df['N_Avaliações'], hue=df['Nota'], palette='viridis', alpha=0.8)
plt.title('Relação entre Preço e Número de Avaliações', fontsize=16)
plt.xlabel('Preço (R$)', fontsize=14)
plt.ylabel('Número de Avaliações', fontsize=14)
plt.legend(title='Nota')
plt.show()

# Mapa de Calor (somente colunas numéricas)
plt.figure(figsize=(10, 8))
numerical_df = df.select_dtypes(include=['float64', 'int64'])  # Selecionar apenas colunas numéricas
correlation_matrix = numerical_df.corr()  # Calcular a correlação
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm')
plt.title('Mapa de Calor das Correlações', fontsize=16)
plt.show()

# Gráfico de Barra
plt.figure(figsize=(8, 6))
df['Marca'].value_counts().head(10).plot(kind='bar', color='green', alpha=0.7)
plt.title('Top 10 Marcas mais Frequentes', fontsize=16)
plt.xlabel('Marca', fontsize=14)
plt.ylabel('Frequência', fontsize=14)
plt.show()

# Gráfico de Pizza
plt.figure(figsize=(8, 6))
df['Gênero'].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, cmap='viridis')
plt.title('Proporção de Produtos por Gênero', fontsize=16)
plt.ylabel('')  # Remover o rótulo do eixo Y
plt.show()

# Gráfico de Densidade
plt.figure(figsize=(8, 6))
sns.kdeplot(df['Preço'], fill=True, color='red', alpha=0.7)
plt.title('Distribuição de Preços', fontsize=16)
plt.xlabel('Preço (R$)', fontsize=14)
plt.ylabel('Densidade', fontsize=14)
plt.show()


# Gráfico de Regressão
plt.figure(figsize=(8, 6))
sns.regplot(x=df['Desconto'], y=df['Preço'], line_kws={'color': 'blue'})
plt.title('Regressão: Preço em função do Desconto', fontsize=16)
plt.xlabel('Desconto (%)', fontsize=14)
plt.ylabel('Preço (R$)', fontsize=14)
plt.show()