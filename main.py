import streamlit as st
from UI import app_ui
from data_cleaning import clean_data
from data_visualization import visualize_data

def main():
    # Display UI elements from UI.py
    df = app_ui()
    
    if df is not None:
        # Clean the data using functions from data_cleaning.py
        df = clean_data(df)
        
        # Visualize the data using functions from data_visualization.py
        visualize_data(df)

if __name__ == "__main__":
    main()
