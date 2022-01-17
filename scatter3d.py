"""
==============
3D scatterplot
==============

Demonstration of a basic scatterplot in 3D.
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import seaborn as sns
import pandas as pd

# Fixing random state for reproducibility
np.random.seed(19680801)
f = pd.read_csv("cluster_result.csv", index_col=0)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.scatter(f['Hashtags'].values, f['Others'].values, f['Keywords'].values, c=[sns.color_palette()[x] for x in f.result])

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
