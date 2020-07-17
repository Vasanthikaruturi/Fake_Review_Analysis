from flask import Flask, redirect, url_for, request, render_template
import numpy as np
import pandas as pd
from promote import promte
from IP import IP_address

app = Flask(__name__)


@app.route('/')
def session():
	return render_template('SE.html')

@app.route('/success',methods=['POST'])
def success():
	if request.method == 'POST':
		user = request.form['nm']
		print(user)
		rslt,dict1=promte(user)
		dict2=IP_address(user)
		lst=[]
		print(dict1)
		for key,value in dict1.items():
			a=rslt[rslt['review_id']==key]
			if value!=0 and dict2[key]!=0:
				b=a['review_body'].tolist()
				lst.append(b)
				print(lst)
		return render_template('spage.html',lst=lst,rslt=rslt)


if __name__ == '__main__':
	app.run()
