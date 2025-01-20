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



![Image](https://github.com/user-attachments/assets/2894af04-25be-4ae6-ba67-ebbfca5b1997)
![Image](https://github.com/user-attachments/assets/73623406-ed20-40eb-8bc1-c278254834bb)
![Image](https://github.com/user-attachments/assets/2fb0b90c-fe1a-472c-9ecf-90774480565a)
![Image](https://github.com/user-attachments/assets/4d1210c0-51bf-477f-bf90-adb1de762c40)
![Image](https://github.com/user-attachments/assets/e751ff6c-d7fc-4e3f-9e36-b26f6e030d2a)
![Image](https://github.com/user-attachments/assets/23e2fc3c-10de-473b-a80a-566994380604)
![Image](https://github.com/user-attachments/assets/8f8cfb7b-1f44-4ef9-858a-ddbaf8533321)
