
import pandas as pd
from sklearn.linear_model import ElasticNet
from sklearn.preprocessing import StandardScaler
import os

df = pd.read_csv("path")
#print(df.head())
#x=df[]
elasnet=ElasticNet(alpha=0.1,l1_ratio=0.5)



#print(df["price"])
###/NO NULL VALUES CAUSE binance jsons prevents nulls
df.replace(to_replace=True,value=1, inplace=True,regex=True)
df.replace(to_replace=False,value=0, inplace=True,regex=True)
#print(df.head())
from datetime import datetime


df['timestamp']=pd.to_datetime(df['timestamp'],unit='ms')
df['hour'] = df['timestamp'].dt.hour
df['minute'] = df['timestamp'].dt.minute
df['seconds'] = df['timestamp'].dt.second
df = df.drop('timestamp', axis=1)
df.to_csv("processed.csv",index=False)
X = df[['quantity', 'buyer_is_maker', 'best_price_match', 'hour', 'minute','seconds']]
Y=df['price']
file_to_delete = "path"

# 2. Safety Check (The 'If' Logic)
if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print(f"Logic Complete. File '{file_to_delete}' has been deleted.")
else:
    print("The file does not exist (it may have already been deleted).")

scalwr=StandardScaler()
xscale=scalwr.fit_transform(X)
print(xscale)
#elasnet.fit(xscale,Y)
#TODO: upto now we store the processed data, next is to push the processed data into a mysql database
# do this until got enough data and then apply scalings




