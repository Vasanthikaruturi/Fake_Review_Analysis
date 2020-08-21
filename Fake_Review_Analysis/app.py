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
		pid = request.form['nm']
		print(user)
		rslt,fake1=promte(pid)
		fake2=IP_address(pid)
		lst=[]
		for i in range(len(rslt)):
			if fake1[i]==0 and fake2[i]==0:
				lst.append(rslt['reviewbody'])
			else if fake1[i]==0:
				lst.append(rslt['reviewbody'])
			else if fake2[i]==0:
				lst.append(rslt['reviewbody'])
		return render_template('spage.html',lst=lst,rslt=rslt)


if __name__ == '__main__':
	app.run()
