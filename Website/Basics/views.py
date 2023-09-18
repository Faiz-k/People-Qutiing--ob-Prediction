from django.shortcuts import render
import pandas as pd
import sklearn 
from sklearn import tree
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
def home(request):
      if(request.method=="POST"):
         data=request.POST
         stag=data.get('stag')
         gender=data.get('gender')
         age=data.get('age')
         industry=data.get('industry')
         profession=data.get('profession')
         traffic=data.get('traffic')
         coach=data.get('coach')
         head_gender=data.get('head_gender')
         greywage=data.get('greywage')
         way=data.get('way')
         extraversion=data.get('extraversion')
         independ=data.get('independ')
         selfcontrol=data.get('selfcontrol')
         anxiety=data.get('anxiety')
         novator=data.get('novator')
         path="C:\\Users\\mf879\\OneDrive\\Desktop\\ml\\ml\\turnover.csv"
         df=pd.read_csv(path,engine='python',encoding='latin1')
         for col in df.columns:
            if df[col].dtype == 'object':
               values = df[col].value_counts()
               values = dict(values)
               label = LabelEncoder()
               label = label.fit(df[col])
               df[col] = label.transform(df[col].astype(str))
        
               new_values = df[col].value_counts()
               new_values = dict(new_values)
        
               value_dict = {}
               i=0
               for key in values:
                  value_dict[key] = list(new_values)[i]
                  i+= 1
         X = df.drop(columns=['event'])
         y = df['event']
         model=tree.DecisionTreeClassifier()
         model.fit(X,y)
         info=model.predict([[stag,gender,age,industry,profession,traffic,coach,head_gender,greywage,way,extraversion,independ,selfcontrol,anxiety,novator]])
         return render(request,"home.html",context={'info':info})
      return render(request,'home.html')



