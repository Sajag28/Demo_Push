import pickle
import pandas as pd
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import accuracy_score,mean_squared_error
from CSE_Data_Match import CSE 
data=pd.read_csv("raw_dataset/Mech_train.csv")
# print(data.columns)
z=data[['No. of Journals', 'FeedBack Level', 'Conference Num']]
y=data['Feedback Score (Out of 1000)']
X_train,X_test,y_train,y_test = train_test_split(z,y,test_size=0.1)
model=LinearRegression()
a=model.fit(X_train,y_train)
print(a)
y_pred=model.predict(X_test)
print("Predicted Y is: \n")
print(y_pred)
# print(accuracy_score(y_test,y_pred))
print(mean_squared_error(y_test,y_pred))

with open('mech_linear_reg_model.pkl', 'wb') as f:
    pickle.dump(model, f)