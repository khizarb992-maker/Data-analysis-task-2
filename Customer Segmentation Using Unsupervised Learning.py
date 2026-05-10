# -*- coding: utf-8 -*-
"""
Created on Sun May 10 12:01:43 2026

@author: Khizar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.metrics import silhouette_score

df =pd.read_csv(r"E:\Mall_customers.csv")
df.head()

df.info()
df.describe()
df.isnull().sum()

sns.countplot(x='Genre', data=df)
plt.title("Genre Distribution")
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(df['Age'], bins=20, kde=True)
plt.title("Age Distribution")
plt.show()

plt.figure(figsize=(8,6))
sns.scatterplot(x='Annual Income (k$)',
                y='Spending Score (1-100)',
                hue='Genre', data=df)
plt.title("Income vs Spending Score")
plt.show()


x = df[['Annual Income (k$)', 'Spending Score (1-100)']]

scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

wcss = []

for i in range(1,11):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(x_scaled)
    wcss.append(kmeans.inertia_)
    
plt.figure(figsize=(8,5))
plt.plot(range(1,11),wcss, marker='o')
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.show()

kmeans = KMeans(n_clusters=5, random_state=42)
df['Cluster'] = kmeans.fit_predict(x_scaled)
df.head()

plt.figure(figsize=(10,6))

sns.scatterplot(x='Annual Income (k$)',
                y='Spending Score (1-100)',
                hue='Cluster', palette='Set2', data=df,
               s=100)

plt.title("Customer Segments")
plt.show()

pca = PCA(n_components=2)

pca_components = pca.fit_transform(x_scaled)

df['PCA1'] = pca_components[:,0]
df['PCA2'] = pca_components[:,1]

plt.figure(figsize=(10,6))

sns.scatterplot(x='PCA1',
                y='PCA2',
                hue='Cluster',
                palette='Set1',
                data=df,
                s=100)
plt.title("PCA Cluster Visualization")
plt.show()

score = silhouette_score(x_scaled,df['Cluster'])
print("Silhouette Score:", score)

df.groupby('Cluster')[['Annual Income (k$)', 'Spending Score (1-100)','Age']].mean()




























































