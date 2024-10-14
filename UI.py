import streamlit as st
import pandas as pd

def app_ui():
    st.title("Data Cleaning and Preprocessing App")

    # File uploader
    uploaded_file = st.file_uploader("Upload only a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        # Read the uploaded CSV file
        df = pd.read_csv(uploaded_file)
        st.write("Data Preview:")
        st.write(df.head())
        return df
    else:
        st.write("Please upload a a CSV file.")
        return None
