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
    st.write(
        "John Doe is a co-founder of the Sepsis Information Hub. With a background in medicine and "
        "passion for healthcare technology, John is dedicated to improving awareness and understanding of sepsis."
    )
    st.write("Connect with John on [LinkedIn](https://www.linkedin.com/in/muhammad-razi-rizzardi-83a49229b/)")

# Team member 2 in the second column
with col2:
    st.header("Fadlurahman Asidiq P")
    st.image(img_fadlu, caption="Fadlu", use_column_width=True)
    st.write(
        "Jane Smith is the lead developer responsible for bringing the Sepsis Information Hub to life. "
        "With expertise in software development, Jane ensures a seamless and user-friendly experience for our visitors."
    )
    st.write("Connect with Jane on [LinkedIn](https://www.linkedin.com/in/janesmith/)")

# Team member 3 in the third column
with col3:
    st.header("Mochammad Haikal A G")
    st.image(img_hekal, caption="Haikal", use_column_width=True)
    st.write(
        "Bob Johnson is our content specialist who ensures that the information provided on the Sepsis Information Hub "
        "is accurate, informative, and accessible. Bob is passionate about health education and awareness."
    )
    st.write("Connect with Bib on [LinkedIn](https://www.linkedin.com/in/bobjohnson/)")

# Footer
st.write(
    "If you have any inquiries or would like to get in touch with our team, please email us at "
    "[contact@sepsisinfohub.com]. We appreciate your interest in our mission."
)
