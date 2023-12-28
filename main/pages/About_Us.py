# Import necessary libraries
import streamlit as st
from PIL import Image

# Page title
st.title("About Us")
img_razi = Image.open("/Users/family/Documents/GitHub/ICU-Deployment/main/assets/razi.png")
img_hekal = Image.open("/Users/family/Documents/GitHub/ICU-Deployment/main/assets/hekal.png")
img_fadlu = Image.open("/Users/family/Documents/GitHub/ICU-Deployment/main/assets/fadlu.png")

# Introduction
st.write(
    "Welcome to the 'About Us' page. Get to know the individuals behind the Sepvisor."
)

# Using st.columns to create three columns
col1, col2, col3 = st.columns(3)

# Team member 1 in the first column
with col1:
    st.header("Muhammad Razi Rizzardi")
    st.image(img_razi, caption="Razi", use_column_width=True)
    st.write("Connect with Razi on [LinkedIn](https://www.linkedin.com/in/muhammad-razi-rizzardi-83a49229b/)")

# Team member 2 in the second column
with col2:
    st.header("Fadlurahman Asidiq P")
    st.image(img_fadlu, caption="Fadlu", use_column_width=True)
    st.write("Connect with Fadlu on [LinkedIn](https://www.linkedin.com/in/janesmith/)")

# Team member 3 in the third column
with col3:
    st.header("Mochammad Haikal A G")
    st.image(img_hekal, caption="Haikal", use_column_width=True)
    st.write("Connect with Haikal on [LinkedIn](https://www.linkedin.com/in/bobjohnson/)")

# Footer
st.write(
    "If you have any inquiries or would like to get in touch with our team, please email us at "
    "[contact@sepsisinfohub.com]. We appreciate your interest in our mission."
)
