import numpy as np
import pandas as pd
import pickle as pkl
import streamlit as st

model = pkl.load(open('MIPML.pkl', 'rb'))

st.header('Medical Insurance Predicted')

gender = st.selectbox('Choose the gender', ['Female', 'Male'])
smoker = st.selectbox('Are you smoker ?', ['Yes', 'No'])
region = st.selectbox('Choose Region', ['Southeast', 'Southwest', 'Northeast', 'Nortwest'])
age = st.slider('Enter Age', 5, 80)
bmi = st.slider('Enter BMI', 5, 100)
children = st.slider('Number No of childrens', 0, 5)

if gender == 'Female':
    gender = 0
else:
    gender = 1
    
if smoker == 'No':
    smoker = 0
else:
    smoker = 1
    
if region == 'Southeast':
    region = 0
if region == 'Southwest':
    region = 1
if region == 'Northeast':
    region = 2
else:
    region = 3
    
input_data = (age, gender, bmi, children, smoker, region)
input_data = np.asarray(input_data)
input_data = input_data.reshape(1, -1)

if st.button('Predict'):
    predicted_pr = model.predict(input_data)

    display_string = 'Medical Insurance Will be  ' + str(round(predicted_pr[0], 2)) + 'USD Dollars'

    st.markdown(display_string)
