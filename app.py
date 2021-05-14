#importing python packages
import streamlit as st
import pandas as pd
import numpy as np
import os
import joblib
import matplotlib.pyplot as plt
import matplotlib
from manage_db import *
import hashlib



#AGG backend is for writing to file, not for rendering in a window.
matplotlib.use('Agg')




#list of columns name
feature_names_best=['age','sex','steroid','antivirals','fatigue','spiders','malaise','anorexia','liver_big','liver_firm','spleen_palpable','ascites','varices','bilirubin','alk_phosphate','sgot','albumin','protime','histology']



#dictionary of gender
gender_dictionary={"male":1,"female":2}



# dictionary of features
feature_dictionary={"yes":1,"no":0}



def get_value(sex_key,my_dict):
	for key,val in my_dict.items():
		if sex_key==key:
			return val



def get_key(val,my_dict):
	for key,val in my_dict.items():
		if val==key:
			return key



def get_feature_value(val):
	feature_dictionary={"yes":1,"no":0}
	for key,value in feature_dictionary.items():
		if val==key:
			return value
			
			
			
# load machine learning models from folder in read binary mode
def load_model(model_file):
	loaded_model=joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model
	
	
	

# to generate secure hashed password so that database admin wont know your password
def generate_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()


	
	
# to verify whether password is same or not
def verify_hashes(real_password,hashed_password):
	if generate_hashes(real_password) == hashed_password:
		return hashed_password
	return False
	



#execution of webapp start from here
def main():

	#to show title on the main page
	st.title("Hepatitis mortality prediction app")


	#list menu and submenu for setting options in list
	menu=["home", "login", "signup"]
	submenu=["plot","prediction"]


	#make a selectbox in the sidebar and pass menu list given above to show choices and return choice
	choice=st.sidebar.selectbox("menu",menu)
	
	
	#if choice is home then show subheader and a text below 
	if choice=="home":
		st.subheader("HOMEPAGE")
		st.text("what is hepatitis disease?")
	
	
	
	#if choice is login then show 2 inputs for username and password and get data from the login form
	elif choice=="login":
	
		#get username and password from the form
		username=st.sidebar.text_input("Username")
		real_password=st.sidebar.text_input("Password",type='password')
  
  
		#make a checkbox in sidebar and if user clicks on checkbox and password is same then pass
		if st.sidebar.checkbox("login"):
			
			#create a user table in the database
			create_user_table()
			
			#generate hashed password and assign
			hashed_password=generate_hashes(real_password)
			
			#call login_user function pass username and returned value of verify_hashes function
			result=check_login(username,verify_hashes(real_password,hashed_password))
			
			
			if result:
				
				#show success message when login succeed
				st.success("welcome {}".format(username))
				
				
				#show text and select box with options from the list of submenu given menu
				activity=st.selectbox("please select from the options given below",submenu)
				
				
				if activity=="plot":
				
					#show subheader text
					st.subheader("show csv file as dataframe")
					
					# read csv file from the folder and convert into pandas dataframe
					df=pd.read_csv("data/clean_hepatitis_dataset.csv")
					
					#show dataframe in webapp
					st.dataframe(df)
					
					# take class column from dataframe then count the number of values and plot bargraph
					df['class'].value_counts().plot(kind='bar')

					
					#show pyplot in webapp
					st.pyplot()
				

					# read csv file and covert into datafram
					freq_df=pd.read_csv("data/freq_df_hepatitis_dataset.csv")
					
					#show bar chart in web app having column name count
					st.bar_chart(freq_df['count'])


					# make a checkbox carry text
					if st.checkbox("area chart"):
						
						#change dataframe columns into list 
						all_columns=df.columns.to_list()
						
						#make a multiselector and pass list given above as argument
						feat_choices=st.multiselect("choose a feature",all_columns)
						
						#make a new list after getting values from the columns selected above
						new_df=df[feat_choices]
						
						#make an area chart using list values from above
						st.area_chart(new_df)
					

				elif activity=="prediction":
				
					#show a subheader with text
					st.subheader("predictive Analytics")


					#set range in input box
					age=st.number_input("age",7,80)
					st.write(age)
					
					#show radio buttons having options given in gender_dictionary above
					sex=st.radio("sex",tuple(gender_dictionary.keys()))
					st.write(sex)
					
					
					#show radio buttons having options given in feature_dictionary above
					steroid=st.radio("Do you take steroid?",tuple(feature_dictionary.keys()))
					st.write(steroid)
					
					#show radio buttons having options given in feature_dictionary above
					antivirals=st.radio("Do you take Antivirals?",tuple(feature_dictionary.keys()))
					st.write(antivirals)
					
					#show radio buttons having options given in feature_dictionary above
					fatigue=st.radio("Do you take fatigue?",tuple(feature_dictionary.keys()))
					st.write(fatigue)
					
					#show radio buttons having options given in feature_dictionary above
					spiders=st.radio("Presence of spider naevi",tuple(feature_dictionary.keys()))
					st.write(spiders)
					
					#show select box having options given in feature_dictionary above 
					ascites=st.selectbox("Ascites",tuple(feature_dictionary.keys()))
					st.write(ascites)
					
					#show select box having options given in feature_dictionary above 
					varices=st.selectbox("presence of varices",tuple(feature_dictionary.keys()))
					st.write(varices)
					
					#show range input
					bilirubin=st.number_input("bilirubin content",0.0,8.0)
					st.write(bilirubin)
					
					#show range input
					alk_phosphate=st.number_input("alkaline phosphate content",0.0,296.0)
					st.write(alk_phosphate)
					
					#show range input
					sgot=st.number_input("Sgot",0.0,648.0)
					st.write(sgot)
					
					#show range input
					albumin=st.number_input("albumin",0.0,6.4)
					st.write(albumin)
					
					#show range input
					Prothrombin=st.number_input("Prothrombin",0.0,100.0)
					st.write(Prothrombin)
					
					#show select box having options given in feature_dictionary
					histology=st.selectbox("Histology",tuple(feature_dictionary.keys()))
					st.write(histology)

					#making a list of features using functions
					feature_list = [age,get_value(sex,gender_dictionary),get_feature_value(steroid),get_feature_value(antivirals),get_feature_value(fatigue),get_feature_value(spiders),get_feature_value(ascites),get_feature_value(varices),bilirubin,alk_phosphate,sgot,albumin,int(Prothrombin),get_feature_value(histology)]
					st.write(feature_list)
					

					#dictionary of list
					pretty_result={"age":age,"sex":sex,"steroid":steroid,"antivirals":antivirals,"spiders":spiders,"ascites":ascites,"varices":varices,"bilirubin":bilirubin,"alk_phosphate":alk_phosphate,"sgot":sgot,"albumin":albumin,"Prothrombin":Prothrombin,"histology":histology}

					#json of pretty result
					st.json(pretty_result)

					#make array of feture_list
					single_sample=np.array(feature_list).reshape(1,-1)

					#make a selectbox carring options given below
					model_choice=st.selectbox("select model",["LR","KNN","DecisionTree"])

					#make button
					if st.button("predict"):
						
						#work if model is KNN
						if model_choice=="KNN":
							
							#load model file from models folder
							loaded_model=load_model("./models/knn_hepB_model.pkl")
							
							#predict from loaded model and store
							prediction=loaded_model.predict(single_sample)
							
							#predict probability from loaded model and store
							pred_prob=loaded_model.predict_proba(single_sample)
						
						#work if model is DecisionTree
						elif model_choice=="DecisionTree":						
							
							loaded_model=load_model("models/decision_tree_clf_hepB_model.pkl")
							
							prediction=loaded_model.predict(single_sample)
							
							pred_prob=loaded_model.predict_proba(single_sample)
							
						#work if model is LR
						else:
						
							loaded_model=load_model("models/logistic_regression_hepB_model.pkl")
							
							prediction=loaded_model.predict(single_sample)
							
							pred_prob=loaded_model.predict_proba(single_sample)
						
						#st.write(prediction)
						#prediction_label={"Die":1,"Live":2}
						#final_result=get_key(prediction,prediction_label)
						#st.write(final_result)
						
						#if prediction came from above is 1 then patient dies
						if prediction==1:
							
							#show warning message
							st.warning("Patient dies")
							
						else:
						
							#show success message
							st.success("Patient lives")
							
							#make a dictionary to store percentage of living or die
							pred_probability_score={"Die":pred_prob[0][0]*100,"Live":pred_prob[0][1]*100}
							
							#show a subheader
							st.subheader("Prediction probability score using {}".format(model_choice))
							
							#show json format in webapp
							st.json(pred_probability_score)
						
						#if st.checkbox("interpret"):
							
						
			else:
				
				#set warning message with text
				st.warning("Incorrect username/Password")
				
	elif choice=="signup":
		
		#get username from input form
		new_username=st.text_input("username")
		
		#get password and confirm password from input form
		new_password=st.text_input("password",type='password')
		confirm_password=st.text_input("confirm password",type='password')
		
		#if password and confirm password same
		if new_password==confirm_password:
		
			#show success message if both password same
			st.success("password is matched")
			
		else:
		
			#show warning message if password not matched
			st.warning("password did not matched")
		
		#show submit button
		if st.button("submit"):
		
			#cal function in manage_db file
			create_user_table()
			
			#call generate hashes function and return hashed password
			hashed_new_password=generate_hashes(new_password)
			
			#call adduserdata function in manage_db file
			add_user_data(new_username,hashed_new_password)
			
			#show success message 
			st.success("you have successfully created a new account")
			
			#show info message
			st.info("please login to start your session")
	
#check if main method
if __name__=='__main__':

	#call main method
	main()


