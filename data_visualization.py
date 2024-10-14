import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def visualize_data(df):
    st.sidebar.title("Data Visualization")

    # Histogram
    if st.sidebar.checkbox("Show Histogram"):
        st.write("Histogram")
        for column in df.select_dtypes(include=['float64', 'int64']).columns:
            plt.figure()
            sns.histplot(df[column], kde=True)
            st.pyplot(plt)

    # Scatter plot  
    if st.sidebar.checkbox("Show Scatter Plot"):
        x_col = st.sidebar.selectbox("X-axis", df.columns)
        y_col = st.sidebar.selectbox("Y-axis", df.columns)
        st.write(f"Scatter plot between {x_col} and {y_col}")
        plt.figure()
        sns.scatterplot(x=df[x_col], y=df[y_col])
        st.pyplot(plt)

    # Correlation heatmap
    if st.sidebar.checkbox("Show Correlation Heatmap"):
        st.write("Correlation Heatmap")
        plt.figure(figsize=(10, 8))
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
        st.pyplot(plt)
