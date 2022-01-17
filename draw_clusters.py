import numpy as np
# from sklearn.datasets import load_digits
# from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import umap.umap_ as umap
# import umap
f = pd.read_csv("cluster_result.csv", index_col=0)
reducer = umap.UMAP()
cluster_data = f[
    [
        "Words",
        "Hashtags",
        "Others",
        "Keywords",
    ]
].values
scaled_cluster_data = StandardScaler().fit_transform(cluster_data)
embedding = reducer.fit_transform(scaled_cluster_data)
print(embedding.shape)
plt.scatter(
    embedding[:, 0],
    embedding[:, 1],
    c=[sns.color_palette()[x] for x in f.result])
plt.gca().set_aspect('equal', 'datalim')
plt.title('UMAP-проекция для набора текстов', fontsize=24)