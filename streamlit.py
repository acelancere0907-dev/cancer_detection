import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set title of the application
st.title("My Streamlit App")

# Load some data
data = pd.read_csv("data.csv")

# Display data
st.dataframe(data)

# Create a plot
plt.plot(data["X"], data["y"])
st.pyplot(plt)
