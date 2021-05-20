#python package for working with streamlit web application
import streamlit as st

#python package for working with dataframe and csv files
import pandas as pd

#python package for working with arrays
import numpy as np

# python package for working with operating system files system
import os

# python package for load machine learning models from the folders
import joblib

# python package to plot graphs
import matplotlib.pyplot as plt
import matplotlib

# importing all functions and classes from database file from same directory
from manage_db import *

# python package to work with on making secure hash passwords
import hashlib

# ??
# import lime
# import lime.lime_tabular

# import app1
# import app2
# import streamlit as st
# PAGES = {
#     "App1": app1,
#     "App2": app2
# }
# st.sidebar.title('Navigation')
# selection = st.sidebar.radio("Go to", list(PAGES.keys()))
# page = PAGES[selection]
# page.app()

# declaring dictionary
male_female_dict={"male":1,"female":2}
yes_no_dict={"yes":1,"no":0}


# defining function to return values from dictionary keys
def get_sex_value(sex_key):
	male_female_dict={"male":1,"female":2}
	for key,value in male_female_dict.items():
		if sex_key==key:
			return value

# defining function to return values from dictionary keys
def get_yes_no_value(yes_no_val):
	yes_no_dict={"yes":1,"no":0}
	for key,value in yes_no_dict.items():
		if yes_no_val==key:
			return value
			

# load machine learning models from folder in read binary mode
def loading_ML_model(model_file_name):
	loaded_model_ML=joblib.load(open(os.path.join(model_file_name),"rb"))
	return loaded_model_ML

# to generate secure hashed password so that database admin wont know your password
def generate_hash_passwords(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

# to verify whether password is same or not
def verify_hash_passwords(real_password,hashed_password):
	if generate_hash_passwords(real_password) == hashed_password:
		return hashed_password
	return False
	

#defination of streamlit webapp
def main():

	col1, col2, col3 = st.sidebar.beta_columns([1,6,1])

	with col1:
		st.write("")

	with col2:
		st.image("img/ggsipu.png",width=200)

	with col3:
		st.write("")

	
	col1, col2, col3 = st.beta_columns([6,6,6])

	with col1:
		st.write("")

	with col2:
		st.image("img/ggsipu.png",width=200)

	with col3:
		st.write("")

	#to show title on the main page and sidebar
	# st.sidebar.title("Hepatitis Mortality Prediction Web App")
	st.title("Hepatitis Mortality Prediction Web App")

	# to show image at sidebar and main page
	# st.sidebar.image('ggsipu.png',width=200)
	# st.image('ggsipu.png')

	#list menu and submenu for setting options in list
	menu=["Home", "Login", "Sign-up"]
	submenu=["Plot","Prediction"]

	#sidebar subheader
	st.sidebar.subheader("Hello, Good Morning Users")
	st.sidebar.subheader("Welcome to the Hepatitis Mortality Prediction Web App created using streamlit in python")

	#make a selectbox in the sidebar and pass menu list given above to show choices and return choice
	choice=st.sidebar.selectbox("To get started, Please select from the options given below:",menu)
	
	
	st.sidebar.subheader("Created by:-")
	st.sidebar.subheader("1.Ashwani Kumar[MCA]")
	st.sidebar.subheader("2.Nitin Sharma[MCA]")
	
	#if choice is home then show subheader and a text below 
	if choice=="Home":
		# st.header("")
		# st.header("")
		# st.header("")
		# st.header("")
		# st.subheader("")
		# st.subheader("")
		# st.subheader("")
		# st.text("")
		# st.write("")
		# st.image("",width=)
		# st.image("",width=)
		# st.image("",width=)
		# st.video()
		# st.slider('Slide me', min_value=0, max_value=10)
		# st.select_slider('Slide to select', options=[1,'2'])
		# st.progress(progress_variable_1_to_100)

		# st.title("Streamlit 101: An in-depth introduction")
		# st.markdown("Welcome to this in-depth introduction to [...].")
		# st.header("Customary quote")
		# st.markdown("> I just love to go home, no matter where I am [...]")

		# pics = {
		# 	"Cat": "https://cdn.pixabay.com/photo/2016/09/24/22/20/cat-1692702_960_720.jpg",
		# 	"Puppy": "https://cdn.pixabay.com/photo/2019/03/15/19/19/puppy-4057786_960_720.jpg",
		# 	"Sci-fi city": "https://storage.needpix.com/rsynced_images/science-fiction-2971848_1280.jpg"
		# }
		# pic = st.selectbox("Picture choices", list(pics.keys()), 0)
		# st.image(pics[pic], use_column_width=True, caption=pics[pic])

		# st.markdown("## Party time!")
		# st.write("Yay! You're done with this tutorial of Streamlit. Click below to celebrate.")
		# btn = st.button("Celebrate!")
		# if btn:
		# 	st.balloons()

		# # make toggle expander
		# optionals=st.beta_expander('Expander',False)
		# optionals.checkbox("")
		# optionals.radio("",["","",""])

		# with st.beta_expander('Expand'):
		# 	st.write('Juicy deets')

		# # add columns
		# name_cols=st.beta_columns(3)
		# name_cols[0].text_inputs("")
		# name_cols[1].text_inputs("")
		# name_cols[2].text_inputs("")

		# create colums
		# col1, col2 = st.beta_columns(2)
		# col1.subheader('Columnisation')
		# col2.text("")

		# #create bold,italic,hyperlink,horizontal
		# st.markdown("helloworld__bold__helloworld_italic__*both*__")
		# st.markdown("google:[google](https://www.google.com)")
		# st.markdown("___")

		# #container 
		# container=st.beta_container()
		# container.write()
		# container.write()



	#if choice is login then show 2 inputs for username and password and get data from the login form
	elif choice=="Login":
	
		#get username and password from the form
		username=st.text_input("Username")
		real_password=st.text_input("Password",type='password')
  
  
		#make a checkbox in sidebar and if user clicks on checkbox and password is same then pass
		if st.button('Login'):
			
			#create a user table in the database
			create_user_table()
			
			#generate hashed password and assign
			hashed_password=generate_hash_passwords(real_password)
			
			#call login_user function pass username and returned value of verify_hash_passwords function
			result=check_login(username,verify_hash_passwords(real_password,hashed_password))
			
			
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
					
					
					#show radio buttons having options given in male_female_dict dictionary above
					sex=st.radio("sex",tuple(male_female_dict.keys()))
					
					
					
					#show radio buttons having options given in yes_no_dict above
					steroid=st.radio("Do you take steroid?",tuple(yes_no_dict.keys()))
					
					
					#show radio buttons having options given in yes_no_dict above
					antivirals=st.radio("Do you take Antivirals?",tuple(yes_no_dict.keys()))
					
					
					#show radio buttons having options given in yes_no_dict above
					fatigue=st.radio("Do you take fatigue?",tuple(yes_no_dict.keys()))
					
					
					#show radio buttons having options given in yes_no_dict above
					spiders=st.radio("Presence of spider naevi",tuple(yes_no_dict.keys()))
					
					
					#show select box having options given in yes_no_dict above 
					ascites=st.selectbox("Ascites",tuple(yes_no_dict.keys()))
					
					
					#show select box having options given in yes_no_dict above 
					varices=st.selectbox("presence of varices",tuple(yes_no_dict.keys()))
					
					
					#show range input
					bilirubin=st.number_input("bilirubin content",0.0,8.0)
					
					
					#show range input
					alk_phosphate=st.number_input("alkaline phosphate content",0.0,296.0)
					
					
					#show range input
					sgot=st.number_input("Sgot",0.0,648.0)
					
					
					#show range input
					albumin=st.number_input("albumin",0.0,6.4)
					
					
					#show range input
					Prothrombin=st.number_input("Prothrombin",0.0,100.0)
					
					
					#show select box having options given in yes_no_dict
					histology=st.selectbox("Histology",tuple(yes_no_dict.keys()))
					

					#making a list of features using functions
					st.subheader("showing list of values returned from above input form")
					feature_list = [age,get_sex_value(sex),get_yes_no_value(steroid),get_yes_no_value(antivirals),get_yes_no_value(fatigue),get_yes_no_value(spiders),get_yes_no_value(ascites),get_yes_no_value(varices),bilirubin,alk_phosphate,sgot,albumin,int(Prothrombin),get_yes_no_value(histology)]
					st.write(feature_list)
					

					#dictionary of list
					st.subheader("showing in json format after conversion from dictionary")
					st.json({"age":age,"sex":sex,"steroid":steroid,"antivirals":antivirals,"spiders":spiders,"ascites":ascites,"varices":varices,"bilirubin":bilirubin,"alk_phosphate":alk_phosphate,"sgot":sgot,"albumin":albumin,"Prothrombin":Prothrombin,"histology":histology})


					#convert into numpy array and show in webapp
					st.subheader("After converting into numpy array:")
					single_sample=np.array(feature_list).reshape(1,-1)
					st.write(single_sample)

					#make a selectbox carring options given below
					model_choice=st.selectbox("select model",["LR","KNN","DecisionTree"])

					#make button and it returns true when clicked
					if st.button("predict"):
						
						#work if model is KNN
						if model_choice=="KNN":
							
							#load model file from models folder
							loaded_model_ML=loading_ML_model("./models/knn_hepB_model.pkl")
							
							#predict from loaded model and store
							prediction=loaded_model_ML.predict(single_sample)
							
							#predict probability from loaded model and store
							pred_prob=loaded_model_ML.predict_proba(single_sample)
						
						#work if model is DecisionTree
						elif model_choice=="DecisionTree":						
							
							loaded_model_ML=loading_ML_model("models/decision_tree_clf_hepB_model.pkl")
							
							prediction=loaded_model_ML.predict(single_sample)
							
							pred_prob=loaded_model_ML.predict_proba(single_sample)
							
						#work if model is LR
						else:
						
							loaded_model_ML=loading_ML_model("models/logistic_regression_hepB_model.pkl")
							
							prediction=loaded_model_ML.predict(single_sample)
							
							pred_prob=loaded_model_ML.predict_proba(single_sample)
						
						
						
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
						
					if st.checkbox("Interpret"):
						if model_choice == "KNN":
							loaded_model_ML = loading_ML_model("models/knn_hepB_model.pkl")
							
						elif model_choice == "DecisionTree":
							loaded_model_ML = loading_ML_model("models/decision_tree_clf_hepB_model.pkl")
							
						else:
							loaded_model_ML = loading_ML_model("models/logistic_regression_hepB_model.pkl")
							

							# loaded_model_ML = loading_ML_model("models/logistic_regression_model.pkl")							
							# 1 Die and 2 Live
							df = pd.read_csv("data/clean_hepatitis_dataset.csv")
							x = df[['age', 'sex', 'steroid', 'antivirals','fatigue','spiders', 'ascites','varices', 'bilirubin', 'alk_phosphate', 'sgot', 'albumin', 'protime','histology']]
							feature_names = ['age', 'sex', 'steroid', 'antivirals','fatigue','spiders', 'ascites','varices', 'bilirubin', 'alk_phosphate', 'sgot', 'albumin', 'protime','histology']
							class_names = ['Die(1)','Live(2)']
							explainer = lime.lime_tabular.LimeTabularExplainer(x.values,feature_names=feature_names, class_names=class_names,discretize_continuous=True)
							# The Explainer Instance
							exp = explainer.explain_instance(np.array(feature_list), loaded_model_ML.predict_proba,num_features=13, top_labels=1)
							exp.show_in_notebook(show_table=True, show_all=False)
							# exp.save_to_file('lime_oi.html')
							st.write(exp.as_list())
							new_exp = exp.as_list()
							label_limits = [i[0] for i in new_exp]
							# st.write(label_limits)
							label_scores = [i[1] for i in new_exp]
							plt.barh(label_limits,label_scores)
							st.pyplot()
							plt.figure(figsize=(20,10))
							fig = exp.as_pyplot_figure()
							st.pyplot()
					else:
						st.warning("some error takes place")					
				
				else:
					st.warning("some error takes place")
									
			else:
				
				#set warning message with text
				st.warning("Incorrect username/Password")
		
		else:
			st.warning("either you did not login to the system or you did not sign up yet")		
			
	elif choice=="Sign-up":
		
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
		if st.button("Sign up"):
		
			#cal function in manage_db file
			create_user_table()
			
			#call generate hashes function and return hashed password
			hashed_new_password=generate_hash_passwords(new_password)
			
			#call adduserdata function in manage_db file
			add_user_data(new_username,hashed_new_password)
			
			#show success message 
			st.success("you have successfully created a new account")
			
			#show info message
			st.info("please login to start your session")
		else:
			st.warning("submit failed")
	
	else:
		st.warning("wrong choice, please choose again")
	
#check if main method
if __name__=='__main__':

	#call main method
	main()


