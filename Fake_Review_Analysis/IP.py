import pandas as pd
data = pd.read_csv('product_review.csv')
def IP_address(productid):
    
    ip_add=data[data['product_id']==productid]['IP address'].values
    
    res={}
    for i in data['review_id']:
        res[i]=1
    
    ip_group=data.groupby("IP address")
    print(ip_group)
    print(type(ip_group))
    """ip_list=data["IP address"].unique().tolist()
    size=len(ip_list)
    print(size)"""
    l=len(ip_add)
    
    def getsentiment(text):
        return 0
    
    for i in range(l):
        reviews=ip_group.get_group(ip_add[i])
        
        
        review_by_dates=reviews.groupby("review_date")
        dates_list=reviews["review_date"].unique().tolist()
        
        for j in range(len(dates_list)):
            review_by_pos=[]
            review_by_neg=[]
            
            review_each_day=review_by_dates.get_group(dates_list[j])
            indices=review_each_day.index.tolist()
            
            for k in range(len(review_each_day)):
                text=review_each_day["review_body"][indices[k]]
                if(getsentiment(text)==0):
                    review_by_neg.append(review_each_day["review_id"][indices[k]])
                else:
                    review_by_pos.append(review_each_day["review_id"][indices[k]])
            """review_by_pos.append('R1MTOG8C9Z45BX')
            review_by_pos.append('R1MTOG8C9Z45BX')
            review_by_pos.append('R1MTOG8C9Z45BX')
            review_by_pos.append('R1MTOG8C9Z45BX')"""
            if(len(review_by_pos)>3):
                for i in review_by_pos:
                    res[i]=0
            print(res)
            if(len(review_by_neg)>3):
                for i in review_by_neg:
                    res[i]=0           
    return(res)
                    
        
    
    
