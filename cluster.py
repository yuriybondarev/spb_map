import re
import string
import pandas as pd
import numpy as np
import sklearn as skl
import nltk
import natasha
import copy
from sklearn.cluster import KMeans

# alph = list(string.ascii_letters+string.digits+string.punctuation+string.printable+string.whitespace+'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ')
alph = list(string.ascii_letters+string.digits+".\"'«»-"+string.whitespace+'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ')

min_words = 15
min_keywords = 3

def tokenize(text):
	res = re.split(r"[ ,:;/\\()\n]", text)
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
		if res[i].startswith("«"):
			res[i] = res[i][1:]
		if res[i].endswith("»"):
			res[i] = res[i][:-1]
		if "«" in res[i] or "»" in res[i]:
			res[i] = res[i].replace("«","")
			res[i] = res[i].replace("»","")
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
	tagged = nltk.pos_tag(tokens)
	names = []
	for i in range(len(tagged)):
		if tagged[i][1]=="NNP" or tagged[i][1]=="NN":
			names.append(tagged[i][0])
	return len(names)

def make_data(ds):
	words = []
	hashtags = []
	others = []
	# ho_to_total = []
	keywords = []
	# likes = []
	# comments = []
	# likes_to_comments = []
	for index, row in ds.iterrows():
		tokens_list = tokenize(str(row['caption']))
		quant_dict = qualify_tokens(tokens_list)
		words.append(quant_dict['words'])
		hashtags.append(quant_dict['hashtags'])
		others.append(quant_dict['other'])
		# ho_to_total.append((quant_dict['hashtags']+quant_dict['other'])/(quant_dict['words']+quant_dict['hashtags']+quant_dict['other']))
		keywords.append(get_keywords_number(qualify_tokens2(tokens_list)['words']))
		# likes.append(row['likescount'])
		# comments.append(row['commentscount'])
		# likes_to_comments.append(row['likescount']/row['commentscount'])
	data = {'Words':words,'Hashtags':hashtags,"Others":others,"Keywords":keywords}  # ,"Likes":likes,"Comments":comments
	df = pd.DataFrame(data)	
	df.to_csv("df_for_clustering.csv")

def cluster(ds):

	kmeans = KMeans(n_clusters=3, init='random', max_iter=100, n_init=1) # , init=np.array([[5.5, 11.5], [10.57, 7.57], [7.5, 15.0]])
	model = kmeans.fit(ds)
	rs = model.labels_.tolist()
	print(set(rs))
	ds_copy = copy.deepcopy(ds)
	ds_copy['result'] = rs
	ds_copy.to_csv('cluster_result.csv')

		
if __name__ == "__main__":
	# ds = pd.read_csv("df_for_clustering_2.csv", sep=",", encoding='utf-8', index_col=0)
	# ds2 = ds.drop(['Likes', 'Comments'],axis=1)
	ds = pd.read_csv("spb_2019_data.csv", index_col="myid")
	make_data(ds)
	ds2 = pd.read_csv("df_for_clustering.csv", sep=",", encoding='utf-8', index_col=0)
	cluster(ds2)