import pandas as pd 
df=pd.read_csv("validation.csv")
print(df.shape)
print(df.columns)
# print(df.head(5))
print(df[['article','highlights']].head(5))