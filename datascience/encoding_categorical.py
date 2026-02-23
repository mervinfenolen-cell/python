import pandas as pd
data={'gender':['male','female','female','male'],'size':['S','M','L','M']}
df=pd.DataFrame(data)
df['gender_code']=df['gender'].map({'male':0,'female':1})
print(df['gender_code'])

df_encoder=pd.get_dummies(df,columns=['size'])
print(df_encoder)