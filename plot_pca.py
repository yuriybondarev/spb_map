# -*- coding: utf-8 -*-
"""
=========================================================
PCA example with Iris Data-set
=========================================================

Principal Component Analysis applied to the Iris dataset.

See `here <https://en.wikipedia.org/wiki/Iris_flower_data_set>`_ for more
information on this dataset.

"""

# Code source: Gaël Varoquaux
# License: BSD 3 clause

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import pandas as pd
from sklearn import decomposition

f = pd.read_csv("cluster_result.csv", index_col=0)
X = f[
    [
        "Words",
        "Hashtags",
        "Others",
        "Keywords",
    ]
].values

fig = plt.figure()
plt.clf()
ax = fig.add_subplot(projection='3d')

pca = decomposition.PCA(n_components=3)
pca.fit(X)
X1 = pca.transform(X)

ax.scatter(X1[:, 0], X1[:, 1], X1[:, 2], c=[sns.color_palette()[x] for x in f.result])

plt.show()
