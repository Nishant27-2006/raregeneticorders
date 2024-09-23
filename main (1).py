
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

# Load the gene expression data (this assumes the data has been extracted)
expression_df = pd.read_csv('GSE38959_gene_expression.csv')

# Clean and normalize the data
expression_df['gProcessedSignal'] = pd.to_numeric(expression_df['gProcessedSignal'], errors='coerce')
expression_df['gBGSubSignal'] = pd.to_numeric(expression_df['gBGSubSignal'], errors='coerce')
expression_df_cleaned = expression_df.dropna(subset=['ProbeName', 'gProcessedSignal', 'gBGSubSignal'])
scaler = MinMaxScaler()
expression_df_cleaned['NormalizedSignal'] = scaler.fit_transform(expression_df_cleaned[['gBGSubSignal']])

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
expression_df_cleaned['Cluster'] = kmeans.fit_predict(expression_df_cleaned[['NormalizedSignal']])

# Visualize the clusters with scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x=expression_df_cleaned.index, y=expression_df_cleaned['NormalizedSignal'], hue=expression_df_cleaned['Cluster'], palette='Set2')
plt.title('K-Means Clustering of Gene Expression Data (3 Clusters)')
plt.xlabel('Gene Index')
plt.ylabel('Normalized Expression Signal')
plt.legend(title='Cluster')
plt.savefig('kmeans_clusters_scatter.png')

# Visualize the clusters with density plot
plt.figure(figsize=(10, 6))
sns.kdeplot(data=expression_df_cleaned, x='NormalizedSignal', hue='Cluster', fill=True, palette='Set2')
plt.title('Density Plot of Normalized Gene Expression Values by Cluster')
plt.xlabel('Normalized Expression Signal')
plt.ylabel('Density')
plt.savefig('kmeans_clusters_density.png')

print("Visualizations saved: 'kmeans_clusters_scatter.png' and 'kmeans_clusters_density.png'")
