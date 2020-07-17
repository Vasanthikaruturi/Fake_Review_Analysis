from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from nlp import preprocess
from sklearn import metrics
from sklearn.externals import joblib
import pandas as pd
import numpy as np
obj1=preprocess()

def getsentiment(inp):
	clean=(obj1.tokenize(inp,0))
	final=clean.split(' ')

	testset=[]
	vocabulary=joblib.load('a.txt')
	length=len(vocabulary)
	for i in range(0,length):
		testset.append(0)

	for i in vocabulary:
		if i in final:
			count=0
			a=vocabulary.index(i)
			count=final.count(i)
			testset[a]=testset[a]+count

	for i in obj1.nottrack:
    		try:
       			a=vocabulary.index(i[0])
       			testset[a]-=2
    		except:
       			continue	

	testset=np.array(testset)
	#predi=gnb.predict(testset)
	forest=joblib.load('b.txt')
	pred=forest.predict(testset.reshape(1,-1))

	return pred
