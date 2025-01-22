import streamlit as st
import pickle


with open('linear_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)
    
study_hours=st.text_input("enter studied hours")
if st.button("predict",type="primary"):
    marks=model.predict([[int(study_hours)]])
    st.write(f"your predicted marks is {marks}")