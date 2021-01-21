# -*- coding: utf-8 -*-
"""Untitled34.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Wx08hDMkUldxXqRBG4OuCGuDAaPjz2sH
"""

import pandas as pd 
import numpy as np
from sklearn.svm import SVC 
from sklearn.naive_bayes import MultinomialNB 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.linear_model import LogisticRegressionCV
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier
import streamlit as st 
import seaborn as sns
import joblib


st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('Hello, Friends. thank you for visiting') 
st.write("""My name is Dera. This is my very first machine learning web-based application. The main idea of this program is to connect machine learning algorithm with website so that the user can use it
""")  
st.write("""Covid 19 is a really pain in the neck for me, because i can't be as free as i was when i am about to have a date with bybyn. but fortunately somehow we managed to survive xoxo
Being a data scientist is one of my biggest dreams, that is why i am trying to participate fighting COVID 19 with data science.
also the models is not in a good shape. model that can be used in this app : 



K Nearest Neighbors  Accuracy :  6.5%
K Nearest Neighbors  Precision : 0.0

Logistic Regression  Accuracy :  23.4%
Logistic Regression  Precision : 0.107

Multinomial Naive Bayes  Accuracy :  21.4%
Multinomial Naive Bayes  Precision : 0.21 

The algorithm used in this app is still in development stage, as the Accuracy only reaches below 25% :( if you are willing to have a discussion feel free to contact me :)  
""")



"""# Let's fill the sidebar with your data"""
""" Press the arrows on the top left screen on your phone"""

age= st.sidebar.selectbox(
    'How Old Are you?',
    ('Age 0-9', 'Age 10-19', 'Age 20-24', '25-59', '60+')
) 

gender = st.sidebar.selectbox(
    'To which gender identity do you most identify',
    ('Female', 'Male', 'Trans')
)

contact= st.sidebar.selectbox(
    'do you recently have a contact with someone?',
    ('Yes, with someone i dont know', 'Yes, with someone i know', 'No')
)

fever = st.sidebar.selectbox(
    'Do you have a Fever recently?',
    ('Yes','No')
) 

tiredness = st.sidebar.selectbox(
    'Do you Feel tired recently?',
    ('Yes','No')
)

drycough = st.sidebar.selectbox(
    'Do you have a dry cough?',
    ('Yes','No')
) 

difficulty = st.sidebar.selectbox(
    'Do you have a difficulty in breathing?',
    ('Yes','No')
) 

sore_throat = st.sidebar.selectbox(
    'Do you feel sore in your throat?',
    ('Yes','No')
)  

Pains = st.sidebar.selectbox(
    'do you feel pain recently?',
    ('Yes','No')
) 

NasalCongestion= st.sidebar.selectbox(
    'Do you feel your nose is congested(Tersumbat)?',
    ('Yes','No')
) 

RunnyNose=st.sidebar.selectbox(
    'Do you have a runny nose(Pilek)?',
    ('Yes','No')
) 

Diarrhea=st.sidebar.selectbox(
    'Do you feel like you are having a diarrhea?',
    ('Yes','No')
) 


def getinput() : 
  user={'Fever' : 0.0, 'Tiredness':0.0, 'Dry-Cough':0.0, 'Difficulty-in-Breathing':0.0,
       'Sore-Throat':0.0, 'None_Sympton':0.0, 'Pains':0.0, 'Nasal-Congestion':0.0,
       'Runny-Nose':0.0, 'Diarrhea':0.0, 'Age_0-9':0.0, 'Age_10-19':0.0, 'Age_20-24':0.0,
       'Age_25-59':0.0, 'Age_60+':0.0, 'Gender_Female':0.0, 'Gender_Male':0.0,
       'Gender_Transgender':0.0, 'Contact_Dont-Know':0.0, 'Contact_No':0.0, 'Contact_Yes':0.0, 'Symptomps_Score':0.0} 
  Symptomps_Score=0.0

  if age=='Age 0-9' : 
    user['Age_0-9']=1.0
  elif age=='Age 10-19' : 
    user['Age_10-19']=1.0
  elif age=='Age 20-24' : 
    user['Age_20-24']=1.0
  elif age=='25-59' : 
    user['Age_25-29']=1.0 
  elif age=='60+' : 
    user['Age_60+']=1.0 
  

  if gender=='Female' : 
    user['Gender_Female']=1.0 
  elif gender=='Male' : 
    user['Gender_Male']=1.0 
  elif gender=='Trans' :
    user['Gender_Transgender']=1.0  

  

  if contact=='Yes, with someone i dont know' : 
    user['Contact_Dont-Know']=1.0 
  elif contact=='Yes, with someone i know' : 
    user['Contact_Yes']=1.0 
  elif contact=='No' : 
    user['Contact_No']=1.0
  
  if fever=='Yes' :
    user['Fever']=1.0 
    Symptomps_Score=Symptomps_Score+1
  if tiredness=='Yes' : 
    user['Tiredness']=1.0  
    Symptomps_Score=Symptomps_Score+1
  if drycough=='Yes' : 
    user['Dry-Cough']=1.0 
    Symptomps_Score=Symptomps_Score+1
  if difficulty=='Yes' : 
    user['Difficulty-in-Breathing']=1.0 
    Symptomps_Score=+1
  if sore_throat=='Yes' : 
    user['Sore-Throat']=1.0 
    Symptomps_Score=Symptomps_Score+1
  if Pains =='Yes' :
    user['Pains']=1.0 
    Symptomps_Score=Symptomps_Score+1
  if NasalCongestion=='Yes' : 
    user['Nasal-Congestion']=1.0
    Symptomps_Score=Symptomps_Score+1
  if RunnyNose =='Yes' : 
    user['Runny-Nose']=1.0
    Symptomps_Score=Symptomps_Score+1
  if Diarrhea=='Yes' : 
    user['Diarrhea']=1.0
    Symptomps_Score=Symptomps_Score+1 
  if Symptomps_Score==0 : 
    user['None_Sympton']=1.0 
  user['Symptomps_Score']=Symptomps_Score
  return user 

"""# What is actually happening behind these apps?"""
"""The App will predict and classify your severity condition. The machine is already trained before using these data below"""
""" this is the head of data, showing only 5 elements of the data. The data is available on kaggle :) """
df=pd.read_csv('Covid19-fix.csv').dropna()
st.write(df.head()) 

"""let's take a look at parameter correlation here"""
sns.heatmap(df.corr(), cmap='coolwarm')
st.pyplot() 
"""It is very hard to identify the biggest parameter that affect the Severity of the disease, that is why i can say that rapid test and swab test is kinda rubbing your wallet :("""

"""# **Label**"""
"""While the target is a class in which the model will try to predict based on the features. in this research, there are four labels such as : """
target=df[['Severity_Mild', 'Severity_Moderate',
       'Severity_None', 'Severity_Severe']]  
label=np.array(target) 
lab=[]
for x in label : 
  if x[0]==1 : 
    lab.append('Severity_Mild') 
  elif x[1]==1 : 
    lab.append('Severity_Moderate') 
  elif x[2]==1 : 
    lab.append('Severity_None') 
  elif x[3]==1 : 
    lab.append('Severity_Severe')
df['Label']=lab

st.write(df['Label'].head())

"""Let's Take a look at the number of the labels we have on our data : """ 
st.write(df['Label'].value_counts())
sns.countplot(df['Label']) 
st.pyplot()
us=getinput()
keys=list(us.keys())
val=list(us.values())
st.write('''These are your input''')
for m,n in zip(keys, val) : 
  st.write(m,n)

"""# Prediction Based On your input"""

model= st.sidebar.selectbox(
    'Select The Model You want to use to predict :' ,
    ('K Nearest Neighbors', 'Logistic Regression','Multinomial Naive Bayes')
)  
mode=joblib.load(model+'.sav') 
res=mode.predict([list(us.values())]) 
st.write('The ',model,' Predicted that you might be : ',res[0])
""" Please note this is not a valid medical result """

