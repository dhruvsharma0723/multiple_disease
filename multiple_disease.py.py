# -*- coding: utf-8 -*-
"""
Created on Sun May 21 00:51:59 2023

@author: HP
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import ai


# loading the saved model

diabetes_model = pickle.load(open('C:/Users/HP/Desktop/Multiple Disease Prediction/Saved Models/diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open('C:/Users/HP/Desktop/Multiple Disease Prediction/Saved Models/heart_disease_model.sav','rb'))

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction and Report Summarizer System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)

# Diabetes Prediction    
if (selected == 'Diabetes Prediction'):
    
    # page titleol
    st.title('Diabetes Prediction Report and Summarizer using AIML')
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    col4, col5, col6 = st.columns(3)
    col7, col8 = st.columns(2)
    
    Pregnancies =  col1.text_input('Number of Pregnancies')
        
    Glucose =   col2.text_input('Glucose Level')
    
    BloodPressure = col3.text_input('Blood Pressure value')
    
    SkinThickness = col4.text_input('Skin Thickness value')
    
    Insulin = col5.text_input('Insulin Level')
    
    BMI = col6.text_input('BMI value')
    
    DiabetesPedigreeFunction = col7.text_input('Diabetes Pedigree Function value')
    
    Age = col8.text_input('Age of the Person')
    
    # code for Prediction
    diab_diagnosis = ''
    
 
    # creating a button for Prediction
    
        #if st.button('Diabetes Test Result'):
        #diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        #if (diab_prediction[0] == 1):
          #diab_diagnosis = 'The person is diabetic'
        #else:
          #diab_diagnosis = 'The person is not diabetic'
        
    #st.success(diab_diagnosis)
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        dis_detect = False
        if diab_prediction[0] == 1:
            dis_detect = True
            diab_diagnosis = 'The person is diabetic'
        else:
          dis_detect = False
          diab_diagnosis = 'The person is not diabetic'
        
        
        st.success(diab_diagnosis)
        st.title('Report Summary and Suggestions:')
        
        if dis_detect == True:
            suggestion = ai.get_suggestions(Age,Pregnancies,SkinThickness,DiabetesPedigreeFunction,Insulin,BloodPressure,BMI,Glucose) 
            st.markdown(suggestion)
            

# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction Report and Summarizer using AIML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col3:
        cp = st.text_input('Chest Pain types')
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col3:
        exang = st.text_input('Exercise Induced Angina')
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
            dis_detect = True
            heart_diagnosis = 'The person is having heart disease'
        else:
            dis_detect = False
            heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
    st.title('Report Summary and Suggestions:')
    
    if dis_detect == True:
            suggestion1 = ai.get_suggestions1(age,sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal) 
            st.markdown(suggestion1)
            