#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import streamlit as st
import matplotlib as plt
import matplotlib.image as mp
import joblib
from sklearn.preprocessing import LabelEncoder




st.set_page_config(page_title= "Heart Disease Detection Mechine learning App",layout = "wide")
st.header("***HEART DISEASE WEB APP***")
image = mp.imread('E:\DATA SCIENCE\LMS\PROJECT\hearth.jpg')
st.image(image)
st.write(
	) 

#BMI	Smoking	AlcoholDrinking	Stroke	PhysicalHealth	MentalHealth	
#DiffWalking	Sex	AgeCategory	Race	Diabetic	PhysicalActivity	GenHealth	SleepTime	Asthma	KidneyDisease	SkinCancer
st.sidebar.write("***CHECK DO YOU HAVE HEART DISEASE?***")

BMI = st.sidebar.number_input("Enter your BMI", 0,100)
Smoking = st.sidebar.radio("Do you smoke?",["Yes","No"])
AlcoholDrinking =st.sidebar.radio("Are you alcoholic?",["Yes","No"]) 
Stroke =st.sidebar.radio("Do you have Stroke?",["Yes","No"])
PhysicalHealth = st.sidebar.number_input("Enter your Physical Heath level", 0,30)
MentalHealth =st.sidebar.number_input("Enter your Mental Heath level", 0,30)
DiffWalking = st.sidebar.radio("Do you DiffWalking?",["Yes","No"]) 
Sex = st.sidebar.radio("Gender",["Male","Female"]) 

AgeCategory = st.sidebar.selectbox("Chose your Age range",['55-59', '80 or older', '65-69', '75-79', '40-44', '70-74',
       '60-64', '50-54', '45-49', '18-24', '35-39', '30-34', '25-29'])
Race = st.sidebar.radio("Which is your race",['White', 'Black', 'Asian', 'American Indian/Alaskan Native','Other', 'Hispanic']) 
Diabetic = st.sidebar.radio("Do you have Diabetic?",["Yes","No"])
PhysicalActivity = st.sidebar.radio("Are you doing Workouts?",["Yes","No"]) 
Asthma = st.sidebar.radio("Do you have Asthma?",["Yes","No"])
KidneyDisease = st.sidebar.radio("Do you have kidney disease?",["Yes","No"]) 
SkinCancer = st.sidebar.radio("Do you have Skin cancer?",["Yes","No"]) 



test = [["BMI","Smoking","AlcoholDrinking","Stroke","PhysicalHealth","MentalHealth","DiffWalking","Sex","AgeCategory","PhysicalActivity","Asthma","KidneyDisease","SkinCancer"]]

test = pd.DataFrame([{"BMI" : BMI,"Smoking" : Smoking,"AlcoholDrinking" : AlcoholDrinking,"Stroke" : Stroke,"PhysicalHealth":PhysicalHealth,"MentalHealth" : MentalHealth, "DiffWalking": DiffWalking, "Sex": Sex, "AgeCategory" : AgeCategory, 
	"Race": Race,"Diabetic": Diabetic , "PhysicalActivity":PhysicalActivity,"Asthma":Asthma,"KidneyDisease" : KidneyDisease,"SkinCancer" : SkinCancer}])

st.write("***PREVIEW OF YOUR DATA***")
st.write(test)

cat = ["Smoking","AlcoholDrinking","Stroke","PhysicalHealth","Diabetic","MentalHealth","DiffWalking","PhysicalActivity","Asthma","KidneyDisease","SkinCancer"]

for x in cat:
	for i in test[x]:
		if i == "Yes":
			test[x] = 1
		else:
			test[x] = 0

for i in test["Sex"]:
	if i == "Male":
		test["Sex"] = 1
	else:
		test["Sex"] = 0

for i in test["AgeCategory"]:
	if i == "25-29":
		test["AgeCategory"] = 1
	elif i == "18-24":
		test["AgeCategory"] = 0
	elif i == "30-34":
		test["AgeCategory"] = 2
	elif i == "35-39":
		test["AgeCategory"] = 3
	elif i == "40-44":
		test["AgeCategory"] = 4
	elif i == "40-44":
		test["AgeCategory"] = 5
	elif i == "45-49":
		test["AgeCategory"] = 5
	elif i == "50-54":
		test["AgeCategory"] = 6
	elif i == "55-59":
		test["AgeCategory"] = 7
	elif i == "60-64":
		test["AgeCategory"] = 8
	elif i == "65-69":
		test["AgeCategory"] = 9
	elif i == "70-74":
		test["AgeCategory"] = 10
	elif i == "75-79":
		test["AgeCategory"] = 11
	else:
	    test["AgeCategory"] = 12	

G = ['American Indian/Alaskan Native', 'Asian', 'Black', 'Hispanic',
       'Other', 'White']


for i in test["Race"]:
	if i ==G[0]:
		test["Race"] = 0
	elif i ==G[1]:
		test["Race"] = 1
	elif i ==G[2]:
		test["Race"] = 2
	elif i ==G[3]:
		test["Race"] = 3
	elif i ==G[4]:
		test["Race"] = 4
	else:
		test["Race"] = 5


model = joblib.load(open('E:\\DATA SCIENCE\\LMS\\PROJECT\\trained_model_s.sav','rb'))


st.write("***RESULT:***")

#st.write(prediction)
def result():
	prediction = model.predict(test)
	if prediction == 0:
		results = "YOU HAVE NO HEART DISEASE"
	else:
		results = "YOU HAVE HEART DISEASE"
	return results


results = result()

btn = st.sidebar.button("Submit",on_click=st.write(results))


# In[ ]:




