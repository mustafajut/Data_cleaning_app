import streamlit as st

def clean_data(df):
    st.sidebar.title("Data Cleaning Options")

    # Handling missing values
    missing_option = st.sidebar.selectbox("Handle Missing Values", ["None", "Drop Missing Values", "Fill with Mean"])
    
    if missing_option == "Drop Missing Values":
        df = df.dropna()
    elif missing_option == "Fill with Mean":
        df = df.fillna(df.mean())

    # Remove duplicates
    remove_duplicates = st.sidebar.checkbox("Remove Duplicates")
    if remove_duplicates:
        df = df.drop_duplicates()

    # Normalize data
    normalize_data = st.sidebar.checkbox("Normalize Data")
    if normalize_data:
        df = (df - df.min()) / (df.max() - df.min())

    st.write("Cleaned Data Preview:")
    st.write(df.head())
    
    return df
