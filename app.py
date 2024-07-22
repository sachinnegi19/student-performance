import streamlit as st
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictPipeline


def predict_math_score(gender, ethnicity, parental_level_of_education, lunch, test_preparation_course, reading_score, writing_score):
    # Dummy prediction logic (replace with your actual model prediction logic)
    data=CustomData(
            gender=gender,
            race_ethnicity=ethnicity,
            parental_level_of_education=parental_level_of_education,
            lunch=lunch,
            test_preparation_course=test_preparation_course,
            reading_score=float(reading_score),
            writing_score=float(writing_score)

    )
    pred_df=data.get_data_as_data_frame()
    print(pred_df)

    predict_pipeline=PredictPipeline()
    results=predict_pipeline.predict(pred_df)
    
    return results[0]  # Example: average of reading and writing scores

# Streamlit app
def main():
    st.title("Student Performance Indicator")

    st.header("Student Math Score Prediction")

    gender = st.selectbox("Gender", ["Select your Gender", "male", "female"])
    if gender == "Select your Gender":
        gender = None
    
    ethnicity = st.selectbox("Race or Ethnicity", ["Select Ethnicity", "group A", "group B", "group C", "group D", "group E"])
    if ethnicity == "Select Ethnicity":
        ethnicity = None

    parental_level_of_education = st.selectbox("Parental Level of Education", ["Select Parent Education", "associate's degree", "bachelor's degree", "high school", "master's degree", "some college", "some high school"])
    if parental_level_of_education == "Select Parent Education":
        parental_level_of_education = None
    
    lunch = st.selectbox("Lunch Type", ["Select Lunch Type", "free/reduced", "standard"])
    if lunch == "Select Lunch Type":
        lunch = None
    
    test_preparation_course = st.selectbox("Test Preparation Course", ["Select Test Course", "none", "completed"])
    if test_preparation_course == "Select Test Course":
        test_preparation_course = None

    reading_score = st.number_input("Reading Score out of 100", min_value=0, max_value=100)
    writing_score = st.number_input("Writing Score out of 100", min_value=0, max_value=100)

    if st.button("Predict your Maths Score"):
        if None in (gender, ethnicity, parental_level_of_education, lunch, test_preparation_course):
            st.error("Please fill in all fields.")
        else:
            math_score = predict_math_score(gender, ethnicity, parental_level_of_education, lunch, test_preparation_course, reading_score, writing_score)
            st.success(f"The predicted math score is: {math_score}")

if __name__ == '__main__':
    main()