import pandas as pd
import numpy as np
data={'price':[100,200,150],'quantity':[2,5,3]}
df=pd.DataFrame(data)
df['total']=df['price']* df['quantity']
print(df['total'])

df['log_price']=np.log(df['price'])
print(df['log_price'])

df['price_level']=pd.cut(df['price'],bins=[0,150,250],labels=['LOW','HIGH'])
print(df['price_level'])

df['price_quantity']=df['price'] * df['quantity']
print(df)

