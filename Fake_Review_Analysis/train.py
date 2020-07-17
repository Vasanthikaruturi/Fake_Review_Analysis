import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics
from nlp import preprocess
from sklearn.externals import joblib

def fun():
	data=pd.read_csv("product_review.csv")
	review=(data['review_body'])
	sentiment=(data['Sentiment'])
	n_size=1500

	obj=preprocess()
	clean=[]
	for i in range(0,n_size):
		clean.append(obj.tokenize(data['review_body'][i],i))

	vectorizer=CountVectorizer()
	trainset=vectorizer.fit_transform(clean).toarray()
	vocabulary=vectorizer.get_feature_names()
	joblib.dump(vocabulary,'a.txt')

	for i in obj.nottrack:
    		try:
       			a=vocabulary.index(i[0])
       			trainset[i[1]][a]-=2
    		except:
       			continue

	forest=RandomForestClassifier(n_estimators=100)
	forest.fit(trainset[0:n_size],data['Sentiment'][0:n_size])
	joblib.dump(forest,'b.txt')

#86.8%
fun()




