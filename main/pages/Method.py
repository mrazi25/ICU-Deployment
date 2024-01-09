# Import necessary libraries
import streamlit as st
from PIL import Image

# Page title
st.title("Implemented Method")

logo_path = "main/assets/sepvisor.jpeg"  # Update this with the correct path to your logo
st.sidebar.image(logo_path)
# Introduction
st.write(
    "The experimental method we use is generally the same or similar to that carried out by Raghu, A (2017) "
    "but we change some existing parameters and hyperparameters such as gamma, hidden layer and others."
)

st.header("State Space")
st.write(
    "We use a continuous state space form as illustrated below"
)
vig1 = "main/assets/state.png"
st.image(vig1, caption="figure 1", use_column_width=False, width=250)

st.divider()
st.header("Action Space")
st.write(
    "We use a discretized action space form as illustrated below"
)
vig2 = "main/assets/act.png"
st.image(vig2, caption="figure 2", use_column_width=False, width=250)

st.divider()
st.header("Data Preprocessing")
st.write(
    "The study utilized patient data from the MIMIC-III v1.4 database, "
    "containing admissions from over 38,600 adults. The focus was on a cohort meeting Sepsis-3 criteria."
    " Demographics, lab values, vital signs, and intake/output events were extracted and aggregated into 4-hour windows."
    " \Missing values were addressed through k-nearest neighbors imputation, resulting in a 47 × 1 feature vector per patient per timestep. "
    "Values exceeding clinical limits were capped and normalized per-feature to zero mean and unit variance. For further details on the features."
)
vig3 = "main/assets/prepro.png"
st.image(vig3, caption="figure 3", use_column_width=False, width=250)

st.divider()
st.header("Dueling Double-Deep Q Network")
st.write(
    "We use a Q Network form as illustrated below"
)
vig4 = "main/assets/DQN.png"
st.image(vig4, caption="figure 4", use_column_width=False, width=250)

st.divider()
text = "©2024 HFR Company. All rights reserved. The content on this website is protected by copyright law."
text2 = "For permission requests, please contact +6287870190448."

# Using HTML tags for text alignment
centered_text = f"<p style='text-align:center'>{text}</p>"
centered_text2 = f"<p style='text-align:center'>{text2}</p>"
st.divider()
# Displaying centered text using st.markdown
st.markdown(centered_text, unsafe_allow_html=True)
st.markdown(centered_text2, unsafe_allow_html=True)