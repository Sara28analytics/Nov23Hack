import streamlit as st
import pandas as pd
import joblib 

df = pd.read_csv('test_2umaH9m.csv')

#categorical columns
department = st.selectbox("Department",pd.unique(df['department']))
region = st.selectbox("Region",pd.unique(df['region']))
education = st.selectbox("Education",pd.unique(df['education']))
gender = st.selectbox("Gender",pd.unique(df['gender']))
recruitment_channel = st.selectbox("recruitment_channel",pd.unique(df['recruitment_channel']))

#numerical_columns:
no_of_trainings = st.number_input("No_of_trainings")
age = st.number_input("Age")
previous_year_rating = st.number_input("Pevious_year_rating")
length_of_service = st.number_input("Length_of_service")
KPIs_met_80 = st.number_input("KPIs_met > 80%")
awards_won = st.number_input("Enter_Awards_won?")
avg_training_score = st.number_input("Avg_training_score")

#map the input to respective column format
inputs ={
    'department': department,
    'region': region,
    'education': education,
    'gender': gender,
    'recruitment_channel': recruitment_channel,
    'no_of_trainings': no_of_trainings,
    'age': age,
    'previous_year_rating': previous_year_rating,
    'length_of_service': length_of_service,
    'KPIs_met >80%': KPIs_met_80,
    'awards_won?': awards_won,
    'avg_training_score': avg_training_score
}

#load the model from the pickle file

model = joblib.load('promote_model_pipeline.pkl')

if st.button('Predict'):
    X_input = pd.DataFrame(inputs,index=[0])
    prediction = model.predict(X_input)
    st.write("The predicted value is:")
    st.write(prediction)


