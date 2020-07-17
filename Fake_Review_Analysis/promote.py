import pandas as pd
from test import getsentiment
data=pd.read_csv("product_review.csv")
#product id
def promte(inp):
	#review of the product id
	basic=data.groupby("product_id")
	rslt=basic.get_group(inp)
	for i in rslt['product_parent']:
		h=i
		break
	fake={}
	for i in rslt['review_id']:
		fake[i]=1
	#groupby customer id
	customer=data.groupby("customer_id")
	customer_list = rslt["customer_id"].unique()
	size=len(customer_list.tolist())
	for i in range(0,size):
		#group by brand of each customer
		brand=customer.get_group(customer_list[i])
		print("\n\n\nbrand\n\n\n",brand)
		#brand of given products
		brands=brand.groupby('product_parent')
		print("\n\n\nbrands\n\n\n",brands)
		product_df=brands.get_group(h)
		p=0
		n=0
		size1=len(product_df)
		if(size1>2):
				for j in product_df.index:
					if product_df['verified_purchase'][j]=='Y':
						break
					else:
						s=getsentiment(product_df['review_body'][j])
						if(s==0):
							n=n+1
						else:
							p+=1
				if p==0 or n==0:
					temp=rslt[rslt['customer_id']==customer_list[i]]
					for k in temp.index:
						fake[temp['review_id'][k]]=0
	return rslt,fake


promte("B00OQMFG1Q");