import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from nltk.stem import PorterStemmer
from sklearn import metrics

class preprocess():
	def __init__(self):
		self.nottrack=[]
	def tokenize(self,sentence,i):
		adj=[]
		j=0
		ps=PorterStemmer()
		t=re.sub("[^ a-zA-Z]"," ",sentence)
		t=t.lower()
		t=re.sub(r"ain't","am not",t)
		t=re.sub(r"isn't","is not",t)
		t=re.sub(r"wasn't","was not",t)
		t=re.sub(r"weren't","were not",t)
		t=re.sub(r"can't","can not",t)
		t=re.sub(r"couldn't","could not",t)
		t=re.sub(r"shouldn't","should not",t)
		t=re.sub(r"won't","will not",t)
		t=word_tokenize(t)
		stop=set(stopwords.words('english'))
		t=[w for w in t if w not in stop or w=='not'] 
		t=[ps.stem(w) for w in t] 
		adj=[w for w,pos in nltk.pos_tag(t) if pos=='JJS' or pos=='JJR' or pos=='JJ' or pos=='VBZ' or pos=='NN' or pos=='VB' or pos=='VBP' or pos=='RBR' or pos=='RBS']
		for w,pos in nltk.pos_tag(t):
			if w=='not':
				j='not'
				continue
			if (pos=='JJ' or pos=='VB' or pos=='JJS' or pos=='JJR') and j=='not':
				j=0
				self.nottrack.append([w,i])
		final_words=" ".join(adj)
		return final_words










