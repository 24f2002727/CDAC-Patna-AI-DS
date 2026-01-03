#importing libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
# from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

#data collection
df=pd.read_csv("/Users/shivamkumar/Desktop/CDAC-Patna-AI-DS/capstone_project/data.csv")  #reading the data set
print(df.head())


#data preprocessing
#1.handeling missing values
df['marks'].fillna(df["marks"].mean(),inplace=True)
df['attendence'].fillna(df["attendence"].mean(),inplace=True)
df['study'].fillna(df["study"].mean(),inplace=True)
# df['status'].fillna(df["marks"].mean())

#2.encoding
encoder=LabelEncoder()
df['status']=encoder.fit_transform(df['status'])

#3.scaling
# scaler=MinMaxScaler()
# df[['marks','attendence','study']]=scaler.fit_transform(df[['marks','attendence','study']])

#4.handelling outliers
# upper_limit=df['marks'].quantile(.95)
# df['marks']=np.where(df['marks']>upper_limit,df['marks'])

#we will separating features and target
X=df[['marks','attendence','study']]
Y=df['status']
# print(df.head())

#data splitting
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

#model architecture
model=LogisticRegression(max_iter=200)

#train the model
model.fit(X_train,Y_train)

# prediction
Y_pred=model.predict(X_test)
# print(np.count_nonzero(Y_test==0))

#prediction to random data
# x=[[25,67,2],[30,65,4]]
# pred=model.predict(x)
# print(pred)

#exporting models predicting capability
def prediction_model(x):
    x=[x]
    output=model.predict(x)
    return output


if __name__=="__main__":
    #when main fn
    print("Test data :\n",X_test,len(X_test),"\n")
    print("Y_predicted:\n",Y_pred,"\n")
    mse=accuracy_score(Y_test,Y_pred)
    conf_matrix=confusion_matrix(Y_test,Y_pred)
    print("Accuracy score:",mse,"\n")
    print("Confusion matrix score:\n",conf_matrix)