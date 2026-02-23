import pandas as pd
data={'age':['25','30','35'],'joined':['2022-01-01','2023-02-15','2024-06-30']}
df=pd.DataFrame(data)
print(df.dtypes)

df['age']=df['age'].astype(int)
print(df.dtypes)
print(df)

df['joined']=pd.to_datetime(df['joined'])
print(df.dtypes)
print(df)

df['age_float']=df['age'].astype(float)
print(df.dtypes)
print(df)

df['group']=['A','B','A']
df['group']=df['group'].astype('category')
print(df.dtypes)
print(df)