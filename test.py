# import pandas as pd

# f1 = open('spb_posts_2019.csv','r', encoding='utf-8')
# df1 = pd.read_csv("spb_posts_2019.csv", sep=",")
# print(set(df1['isad']))
# id,shortcode,imageurl,isvideo,caption,commentscount,timestamp,likescount,isad,authorid,locationid,lat,lon
# print(set(df1['caption'][0]))
# df2 = df1.query("isad != 'f'")
# df2.to_csv("spb_posts_2019_ads.csv")
# input()

import numpy as np
# from sklearn.datasets import load_digits
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# import umap
f = pd.read_csv("cluster_result.csv", index_col=0)

plt.scatter(
    f["Words"].values,
    f['Keywords'].values,
    c=[sns.color_palette()[x] for x in f.result])
plt.gca().set_aspect('equal', 'datalim')
plt.title('UMAP-проекция для набора текстов', fontsize=24)
plt.show()