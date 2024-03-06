import pandas as pd
import numpy as np
import datasets as datasets
def func():
   data=pd.read_csv("raw_dataset/Mech_Train.csv")
   param=data.shape[1]
   data["num_id"]=data["Professor Id"]
   k=1
   r=data.shape[0]
   for i in range(data.shape[0]):
      data["num_id"]=range(1,r+1)
      k=k+1
   data["FeedBack"]=data["FeedBack"].replace({
      4.7:"Excellent",
      '4.9':"Outstanding",
      '5':"Outstanding",
      '4.8':"Excellent",
      '4.6':"Very Good",
      '4.5':"Very Good",
      '4.4':"Good",
      '4.3':"Good",
      '4.2':"Good",
      '4.1':"Good",
      '4':"Good"
   })
   data["FeedBack Level"] = data["FeedBack"].replace({
        "Very Good":2,
        "Excellent": 3,
        "Outstanding": 4,
        "Good": 1
    })
   data["Conference"]=data["Conference"].replace({
      3.8:"National",
      3.9:"International",
      4:"National",
      4.1:"International",
      4.2:"National",
      4.3:"International",
      4.4:"National",
      4.5:"International",
      4.6:"National",
      4.7:"International",
   })
   data["Conference Num"]=data["Conference"].replace({
      'International':1,
      'National':2
   })
  
   data.to_csv("raw_dataset/Mech_train.csv", index=False)
   print(data.iloc[64:91])
data=pd.read_csv("raw_dataset/Mech_train.csv")

def CSE(data, domain, department):
    filtered_data = data[(data["Department"] == department) & (data["Domains"].str.contains(domain))]
    return filtered_data

func()









