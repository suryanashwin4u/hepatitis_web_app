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
gender_dict={"male":1,"female":2}

# dictionary of features
feature_dict={"yes":1,"no":0}

def get_value(val,my_dict):
	for key,val in my_dict.items():
		if val==key:
			return val

def get_key(val,my_dict):
	for key,val in my_dict.items():
		if val==key:
			return key

def get_feature_value(val):
	feature_dict={"no":0,"yes":1}
	for key,val in feature_dict.items():
		if val==key:
			return val
# load ml models
def load_model(model_file):
	loaded_model=joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model

# to generate hashed password
def generate_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

# to verify hashes 
def verify_hashes(password,hashed_text):
	if generate_hashes(password) == hashed_text:
		return hashed_text
	return False
	
	
#execution of webapp start from here
def main():
	#to show title on the main page
	st.title("Hepatitis mortality prediction app")

	#set menu and submenu
	menu=["home", "login", "signup"]
	submenu=["plot","prediction"]

	#make a selectbox in the sidebar and pass menu list given above to show choices and select choice
	choice=st.sidebar.selectbox("menu",menu)
	
	#if choice is home then show subheader and a text below 
	if choice=="home":
		st.subheader("HOMEPAGE")
		st.text("what is hepatitis disease?")
	
	#if choice is login then show 2 inputs for username and password and get data from the user
	elif choice=="login":
		username=st.sidebar.text_input("Username")
		password=st.sidebar.text_input("Password",type='password')
  
		#make a checkbox in sidebar and if user clicks on checkbox and password is same then pass
		if st.sidebar.checkbox("login"):
			create_user_table()
			hashed_password=generate_hashes(password)
			result=login_user(username,verify_hashes(password,hashed_password))
			if result:
				st.success("welcome {}".format(username))
				activity=st.selectbox("please select from the options given below",submenu)
				if activity=="plot":
					st.subheader("data vis plot")
					
					# read csv file and show dataframe
					df=pd.read_csv("data/clean_hepatitis_dataset.csv")
					st.dataframe(df)
					
					# take class column from dataframe and count values and plot bargraph
					df['class'].value_counts().plot(kind='bar')
					st.pyplot()

					# read csv file and show barchart
					freq_df=pd.read_csv("data/freq_df_hepatitis_dataset.csv")
					st.bar_chart(freq_df['count'])

					# make a checkbox , multiselector to show area chart of particular columns
					if st.checkbox("area chart"):
						all_columns=df.columns.to_list()
						feat_choices=st.multiselect("choose a feature",all_columns)
						new_df=df[feat_choices]
						st.area_chart(new_df)
					

				elif activity=="prediction":
					st.subheader("predictive Analytics")

					#set number limit in input box
					age=st.number_input("age",7,80)
					sex=st.radio("sex",)




			else:
				st.warning("Incorrect username/Password")
				
	elif choice=="signup":

		new_username=st.text_input("username")
		new_password=st.text_input("password",type='password')
		confirm_password=st.text_input("confirm password",type='password')
		
		if new_password==confirm_password:
			st.success("password is matched")
		else:
			st.warning("password did not matched")
		
		if st.button("submit"):
			create_user_table()
			hashed_new_password=generate_hashes(new_password)
			add_user_data(new_username,hashed_new_password)
			st.success("you have successfully created a new account")
			st.info("please login to start your session")
			
if __name__=='__main__':
	main()


