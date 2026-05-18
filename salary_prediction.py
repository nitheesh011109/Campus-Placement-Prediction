import numpy as np 
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn.metrics import mean_absolute_error , r2_score
import warnings
warnings.filterwarnings("ignore")
df=pd.read_csv('Salary_prediction_data.csv')
df=df.loc[:,~df.columns.str.contains('^Unnamed')]
df.fillna(0,inplace=True)
df = df[df['PlacementStatus'] == 'Placed']
x=df.drop(['StudentId','salary'],axis=1)
y=df['salary']         
le = preprocessing.LabelEncoder()
x['Internship']=le.fit_transform(x['Internship'])
x['Hackathon']=le.fit_transform(x['Hackathon'])   
x['PlacementStatus']=le.fit_transform(x['PlacementStatus'])      
x_train , x_test , y_train , y_test = train_test_split(x,y,test_size=0.3,random_state=100)
model = LinearRegression()
model.fit(x_train,y_train)
ypred = model.predict(x_test)
print("R2 Score:",r2_score(y_test,ypred))
print("Mean Absolute Error:",mean_absolute_error(y_test,ypred))
pickle.dump(model, open('model1.pkl','wb'))
model1=pickle.load(open('model1.pkl','rb'))
predicted_salary = model1.predict([[8,1,3,2,9,4.8,0,1,71,87,0,1]])
print(f"Predicted Salart:₹{int(predicted_salary[0]):,}")