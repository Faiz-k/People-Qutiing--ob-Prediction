import pandas as pd
path="C:\\Users\\mf879\\OneDrive\\Desktop\\Murshid\\turnover.csv"
df=pd.read_csv(path,engine='python',encoding='latin1')
print(df)