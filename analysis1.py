import sys
sys.stdout.reconfigure(encoding='utf-8')
import re
import string
import pandas as pd
import numpy as np
# import sklearn as skl
import nltk
import natasha
import copy
# from sklearn.cluster import KMeans

# string.punctuation+string.printable
# and not(re.match(r"[!\"#$%&\\\'()*+,-./:;<=>?@[\\]^_`{|}~ ]", tagged[i][1]))
alph = list(string.ascii_letters+string.digits+".\"'«»"+string.whitespace+'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ')
# можливо треба прибрати @

def tokenize(text):
	res = re.split(r"[ .,:;()\n]", text) # прибрати крапку
	res = list(filter(lambda x: x != '', res))
	for i in range(len(res)):
		if not(res[i].startswith("@")) and "." in res[i]:
			rt = res[i].split(".")
			res[i] = copy.deepcopy(rt[0])
			res += rt[1:]
		if res[i].startswith("\""):
			res[i] = res[i][1:]
		if res[i].endswith("\""):
			res[i] = res[i][:-1]
	return res

def qualify_tokens(list_tokens):
	res = {'words':0, 'hashtags':0, 'other':0}
	for i in list_tokens:
		if i.startswith('#'):
			res['hashtags'] += 1
		else:
			if all(j in alph for j in i):
				res['words'] += 1
			else:
				res['other'] += 1
	return res

def qualify_tokens2(list_tokens):
	res = {'words':[], 'hashtags':[], 'other':[]}
	for i in list_tokens:
		if i.startswith('#'):
			res['hashtags'].append(i)
		else:
			if all(j in alph for j in i):
				res['words'].append(i)
			else:
				res['other'].append(i)
	return res
	
def get_keywords_number(list_tokens):
	text = " ".join(list_tokens)
	tokens = nltk.word_tokenize(text)
	# print(tokens)
	tagged = nltk.pos_tag(tokens)
	print(tagged)
	names = []
	for i in range(len(tagged)):
		if (tagged[i][1]=="NNP" or tagged[i][1]=="NN"):
			names.append(tagged[i][0])
	print(names)
	return len(names)

f = pd.read_csv("cluster_result.csv", index_col=0)
f1 = f.query("result == 0")
f2 = f.query("result == 1")
f3 = f.query("result == 2")
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
"2_max": f3.max()})
print(dfr)
dfr.to_excel("stat.xlsx")
df = pd.read_csv("spb_2019_data.csv", index_col="myid")
df = df.join(f)
# print(df['Keywords'])
# df['result'] = f['result']
# df['Keywords'] = f['Keywords']
# print(df.index)
for i,d in df.iterrows():
	if d['Words'] < d['Keywords']:
		print(i)
		print(d['result'])
		ct = tokenize(d['caption'])
		ct_cl = qualify_tokens2(ct)
		print(ct_cl['words'])
# print(t_text)
#ltok = tokenize(t_text)
#qt1 = qualify_tokens2(ltok)
# print(qt1)
# print(get_keywords_number(qt1['words']))
# print(df.columns)
# df.to_csv("cluster_results_full.csv")
