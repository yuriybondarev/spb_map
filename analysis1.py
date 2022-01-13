import sys
sys.stdout.reconfigure(encoding='utf-8')
import re
import string
import pandas as pd
import numpy as np
# import sklearn as skl
import cluster
import nltk
import natasha
import copy
# from sklearn.cluster import KMeans


f = pd.read_csv("cluster_result.csv", index_col=0)
f1 = f.query("result == 0")
f2 = f.query("result == 1")
f3 = f.query("result == 2")
f4 = f.query("result == 3")
dfr = pd.DataFrame.from_dict({"0_median": f1.median(), 
"0_mean": f1.mean(), 
"0_min":f1.min(), 
"0_max": f1.max(), 
"1_median": f2.median(), 
"1_mean": f2.mean(), 
"1_min":f2.min(), 
"1_max": f2.max(), 
"2_median": f3.median(), 
"2_mean": f3.mean(), 
"2_min":f3.min(), 
"2_max": f3.max(),
"3_median": f4.median(), 
"3_mean": f4.mean(), 
"3_min":f4.min(), 
"3_max": f4.max()})
print(dfr)
# dfr.to_excel("stat.xlsx")
df = pd.read_csv("spb_2019_data.csv", index_col="myid")
df = df.join(f)

# for i,d in df.iterrows():
	# if d['Words'] < d['Keywords']:
		# print(i)
		# print(d['result'])
		# ct = cluster.tokenize(d['caption'])
		# ct_cl = cluster.qualify_tokens2(ct)
		# print(ct_cl['words'])

# df.to_csv("cluster_results_full.csv")
# df2 = df.query("Words >= Keywords and result == 2")
df2 = df.query("result == 2")
print(len(df2))
print(df.groupby(['result']).count())
df2.to_csv("for_dataset_2.csv")
# for i,d in df2.iterrows():
	# with open("input.txt","a", encoding="utf-8") as inf:
		# inf.write(d['caption'])
		# inf.write("\n\n")
