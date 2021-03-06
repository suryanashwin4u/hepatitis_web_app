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
	# loaded_model_ML=joblib.load(open(os.path.join(model_file_name),"rb"))
	return loaded_model_ML

# to generate secure hashed password so that database admin wont know your password
def generate_hash_passwords(get_password):
	return hashlib.sha256(str.encode(get_password)).hexdigest()

# to verify whether get_password and hashed password is same or not
def verify_hash_passwords(get_password,hashed_password):
	if generate_hash_passwords(get_password) == hashed_password:
		return hashed_password
	return False

#execution starts here
def main():
	
 	# set images in middle at the sidebar
	col1, col2, col3 = st.sidebar.beta_columns([1,6,1])
	with col1:
		st.write("")
	with col2:
		st.image("img/ggsipu.png",width=200)
	with col3:
		st.write("")

	# set images in middle at the homepage
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

	#list menu and submenu for setting options in the list
	sidebar_menu=["1.Project-Introduction","2.Home-Page", "3.Login-Form", "4.Sign-up-Form"]
	homepage_menu=["1.Check-Plot","2.Check-Prediction"]

	#sidebar subheader
	
	#make a selectbox in the sidebar and pass menu list given above to show choices and return choice
	menu_selected=st.sidebar.selectbox("To get started, Please select from the options given below:",sidebar_menu)
	
 
	if menu_selected=="1.Project-Introduction":
		st.subheader("Hello, Good Morning Users")
		st.subheader("Welcome to the Hepatitis Mortality Prediction Web Application created using streamlit and other python libraries, which will take inputs of dignosed data and predicts whether patient would live or die using various various machine learning models like linear regression, KNN, etc")
		st.subheader("Created by:-")
		st.subheader("1.Name: Ashwani Kumar  [MCA],  Roll no: 40216404518")
		st.subheader("2.Name: Nitin Sharma   [MCA],  Roll no: 40916404518")

	#if choice is home then show subheader and a text below 
	elif menu_selected=="2.Home-Page":
		st.image("./img/Awareness-Banner.png",width=700)
		st.video('https://youtu.be/IxCelFhuhQo')
		st.header("what is hepatitis and which organ it effects?".upper())
		st.subheader("Hepatitis is inflammation of the liver. Inflammation is swelling that happens when tissues of the body are injured or infected. It can damage your liver. This swelling and damage can affect how well your liver functions. Hepatitis can be an acute (short-term) infection or a chronic (long-term) infection. Some types of hepatitis cause only acute infections. Other types can cause both acute and chronic infections.")
		st.header("what are its causes?".upper())
		st.subheader("There are different types of hepatitis, with different causes: Viral hepatitis is the most common type. It is caused by one of several viruses -- hepatitis viruses A, B, C, D, and E. In the United States, A, B, and C are the most common. Alcoholic hepatitis is caused by heavy alcohol use Toxic hepatitis can be caused by certain poisons, chemicals, medicines, or supplements Autoimmune hepatitis is a chronic type in which your body's immune system attacks your liver. The cause is not known, but genetics and your environment may play a role.")
		st.header("How is viral hepatitis spread?".upper())		
		st.subheader("Hepatitis A and hepatitis E usually spread through contact with food or water that was contaminated with an infected person's stool. You can also get hepatitis E by eating undercooked pork, deer, or shellfish. Hepatitis B, hepatitis C, and hepatitis D spread through contact with the blood of someone who has the disease. Hepatitis B and D may also spread through contact with other body fluids. This can happen in many ways, such as sharing drug needles or having unprotected sex.")
		st.image("./img/hepatitis_body.jpg",width=700)
		st.header("Who is at risk for hepatitis?".upper())		
		st.subheader("The risks are different for the different types of hepatitis. For example, with most of the viral types, your risk is higher if you have unprotected sex. People who drink a lot over long periods of time are at risk for alcoholic hepatitis.")
		st.header("What are the symptoms of hepatitis?".upper())		
		st.subheader("Some people with hepatitis do not have symptoms and do not know they are infected. If you do have symptoms, they may include Fever, Fatigue, Loss of appetite, Nausea and/or vomiting, Abdominal pain, Dark urine, Clay-colored bowel movements, Joint pain, Jaundice, yellowing of your skin and eyes. If you have an acute infection, your symptoms can start anywhere between 2 weeks to 6 months after you got infected. If you have a chronic infection, you may not have symptoms until many years later.")
		st.header("What other problems can hepatitis cause?".upper())		
		st.subheader("Chronic hepatitis can lead to complications such as cirrhosis (scarring of the liver), liver failure, and liver cancer. Early diagnosis and treatment of chronic hepatitis may prevent these complications.")
		st.header("How is hepatitis diagnosed?".upper())
		st.subheader("To diagnose hepatitis, your health care provider 1.Will ask about your symptoms and medical history ,2.Will do a physical exam, 3.Will likely do blood tests, including tests for viral hepatitis , 4.Might do imaging tests, such as an ultrasound, CT scan, or MRI, 5.May need to do a liver biopsy to get a clear diagnosis and check for liver damage")
		st.image("./img/Hepatitis_A_Symptoms.jpeg",width=700)
		st.header("What are the treatments for hepatitis?".upper())
		st.subheader("Treatment for hepatitis depends on which type you have and whether it is acute or chronic. Acute viral hepatitis often goes away on its own. To feel better, you may just need to rest and get enough fluids. But in some cases, it may be more serious. You might even need treatment in a hospital. There are different medicines to treat the different chronic types of hepatitis. Possible other treatments may include surgery and other medical procedures. People who have alcoholic hepatitis need to stop drinking. If your chronic hepatitis leads to liver failure or liver cancer, you may need a liver transplant.")
		st.header("Can hepatitis be prevented?".upper())		
		st.subheader("There are different ways to prevent or lower your risk for hepatitis, depending on the type of hepatitis. For example, not drinking too much alcohol can prevent alcoholic hepatitis. There are vaccines to prevent hepatitis A and B. Autoimmune hepatitis cannot be prevented.")
		st.image("./img/Top-banner-april-2020-2.png",width=700)

	#if choice is login then show 2 inputs for username and password and get data from the login form
	elif menu_selected=="3.Login-Form":
		
  		#get username and password from the form
		get_username=st.text_input("Username:")
		get_password=st.text_input("Password:",type='password')

		# if login button is clicked then it returns true and following code executes
		if st.button('Login'):

			#generate hashed password
			hashed_password=generate_hash_passwords(get_password)

			#returns true if user already exists else false
			login_check=check_login(get_username,hashed_password)

			if login_check:

				#show success message when login succeed
				st.success("welcome '{}' to the hepatitis mortality prediction webapp".format(get_username.upper()))

				#show text and select box with options from the list of submenu given menu
				activity_selected=st.selectbox("please select from the options given below:".upper(),homepage_menu)

				# if checkplot activity selected from options then following code executes
				if activity_selected=="1.Check-Plot":

					#show subheader text
					st.subheader("showing csv file as dataframe which is used for getting data".upper())

					# read csv file from the folder and convert into pandas dataframe
					pd_dataframe=pd.read_csv("data/clean_hepatitis_dataset.csv")

					#show dataframe in webapp
					st.dataframe(pd_dataframe)

					# take class column from dataframe then count the number of values and plot bargraph
					pd_dataframe['class'].value_counts().plot(kind='bar')

					#show subheader text
					st.subheader("showing bar graph for the number of patients belongs to class 1 and 2".upper())
	
					#show pyplot in webapp
					st.pyplot()

					# read csv file and convert into dataframe
					freq_dataframe=pd.read_csv("data/freq_df_hepatitis_dataset.csv")
	
					#show subheader text
					st.subheader("showing bar chart for count vs age(0-150 years)".upper())

					#show bar chart in web app having column name count
					st.bar_chart(freq_dataframe['count'])
		
#*********************************bug portion 1******************************************
					#make a multiselector and pass list column names as arguments for options list
					columns_names=pd_dataframe.columns.to_list()
					# feature_selected=st.multiselect("choose a feature from the following list to show more results:".upper(),columns_names)
					
					#make a new list after getting values from the columns selected above
					new_column_dataframe=pd_dataframe[columns_names]
					
					#show dataframe in webapp
					# st.dataframe(new_column_dataframe)
					# st.dataframe(pd_dataframe[feature_selected])

					#make an area chart using list values from above
					st.subheader("showing a frequency graph of all the columns in the dataframe".upper())
					
					st.area_chart(new_column_dataframe)
					# st.area_chart(pd_dataframe[feature_selected])

#  ******************************bug portion 1 ending*****************************************					
#  ******************************bug portion 2 starts*****************************************					
				elif activity_selected=="2.Check-Prediction":

					#show a subheader with text
					st.subheader("Prediction Analytics, here you can input your dygnostic details to get prediction".upper())

					#set range in input box
					age=st.number_input("age".upper(),7,80)

					#show radio buttons having options given in male_female_dict dictionary above
					sex=st.radio("sex".upper(),tuple(male_female_dict.keys()))

					#show radio buttons having options given in yes_no_dict above
					steroid=st.radio("Do you take steroid?".upper(),tuple(yes_no_dict.keys()))


					#show radio buttons having options given in yes_no_dict above
					antivirals=st.radio("Do you take Antivirals?".upper(),tuple(yes_no_dict.keys()))


					#show radio buttons having options given in yes_no_dict above
					fatigue=st.radio("Do you have fatigue?".upper(),tuple(yes_no_dict.keys()))


					#show radio buttons having options given in yes_no_dict above
					spiders=st.radio("Presence of spider naevi".upper(),tuple(yes_no_dict.keys()))


					#show select box having options given in yes_no_dict above 
					ascites=st.selectbox("Ascites".upper(),tuple(yes_no_dict.keys()))


					#show select box having options given in yes_no_dict above 
					varices=st.selectbox("presence of varices".upper(),tuple(yes_no_dict.keys()))


					#show range input
					bilirubin=st.number_input("bilirubin content".upper(),0.0,8.0)


					#show range input
					alk_phosphate=st.number_input("alkaline phosphate content".upper(),0.0,296.0)


					#show range input
					sgot=st.number_input("Sgot".upper(),0.0,648.0)


					#show range input
					albumin=st.number_input("albumin".upper(),0.0,6.4)


					#show range input
					Prothrombin=st.number_input("Prothrombin".upper(),0.0,100.0)


					#show select box having options given in yes_no_dict
					histology=st.selectbox("Histology".upper(),tuple(yes_no_dict.keys()))


					#making a list of features using functions
					st.subheader("showing list of values returned from above input form".upper())
					feature_list = [age,get_sex_value(sex),get_yes_no_value(steroid),get_yes_no_value(antivirals),get_yes_no_value(fatigue),get_yes_no_value(spiders),get_yes_no_value(ascites),get_yes_no_value(varices),bilirubin,alk_phosphate,sgot,albumin,int(Prothrombin),get_yes_no_value(histology)]
					st.write(feature_list)


					#dictionary of list
					st.subheader("showing in json format after conversion from dictionary".upper())
					st.json({"age":age,"sex":sex,"steroid":steroid,"antivirals":antivirals,"spiders":spiders,"ascites":ascites,"varices":varices,"bilirubin":bilirubin,"alk_phosphate":alk_phosphate,"sgot":sgot,"albumin":albumin,"Prothrombin":Prothrombin,"histology":histology})


					#convert into numpy array and show in webapp
					st.subheader("After converting into numpy array:".upper())
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
							st.warning("Patient dies".upper())

						else:

							#show success message
							st.success("Patient lives".upper())

							#make a dictionary to store percentage of living or die
							pred_probability_score={"Die":pred_prob[0][0]*100,"Live":pred_prob[0][1]*100}

							#show a subheader
							st.subheader("Prediction probability score using {}".upper().format(model_choice))

							#show json format in webapp
							st.json(pred_probability_score)

						if st.checkbox("Interpret".upper()):
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
							st.warning("some error takes place".upper())					

				else:
					st.warning("some error takes place".upper())

			else:

				#set warning message with text
				st.warning("Incorrect username/Password".upper())

		else:
			st.warning("either you did not login to the system or you did not sign up yet".upper())		
   
#    ********************************bug 2 ending*******************************************

	elif menu_selected=="4.Sign-up-Form":

		#get username from input box
		new_username=st.text_input("username".upper())

		#get password from input box
		new_password=st.text_input("password".upper(),type='password')
	
		#get confirm password from input box
		confirm_password=st.text_input("confirm password".upper(),type='password')

		#if password and confirm password same
		if new_password==confirm_password and new_password!='' and confirm_password!='':

			#show success message if both password same
			st.success("password completely matched".upper())

		elif new_password=='' or confirm_password=='' :

			#show warning message if password not matched
			st.warning("either password box or confirm password box is empty, please fill before going ahead".upper())
   
		else:

			#show warning message if password not matched
			st.warning("password and confirm password did not matched".upper())

		#show submit button
		if st.button("Sign up".upper()):

			#cal function in manage_db file
			create_table_db()

			#call generate hashes function and return hashed password
			hashed_new_password=generate_hash_passwords(new_password)

			#call adduserdata function in manage_db file
			warning_if_any=add_user_db(new_username,hashed_new_password)
   
			if warning_if_any:
				st.warning(warning_if_any.upper())
				
			else:
				#show success message 
				st.success("new account has been created".upper())

				#show info message
				st.info("please choose login-form option from sidebar to login and start your session".upper())
   
		else:
			st.warning("either you did not click sign up button or some failure occurs".upper())

	else:
		st.warning("wrong choice, please choose again".upper())

#check if main method
if __name__=='__main__':

	#call main method
	main()


