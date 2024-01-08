# Import necessary libraries
import streamlit as st
from PIL import Image

# Page title
st.title("MIMIC-III Dataset Information")

logo_path = "main/assets/sepvisor.jpeg"  # Update this with the correct path to your logo
st.sidebar.image(logo_path)
# Introduction
st.write(
    "The MIMIC-III (Medical Information Mart for Intensive Care III) dataset is a widely used "
    "publicly available dataset that contains de-identified health data for patients admitted to "
    "the intensive care unit (ICU). This page provides an overview of the MIMIC-III dataset."
)

# About MIMIC-III
st.header("About MIMIC-III")
st.write(
    "MIMIC-III is a database developed by the Massachusetts Institute of Technology (MIT) "
    "that includes clinical data from patients admitted to the Beth Israel Deaconess Medical Center in Boston, USA. "
    "The dataset covers a wide range of information, including demographics, vital signs, laboratory test results, "
    "medication orders, and more."
)

# Accessing the dataset
st.header("Accessing the Dataset")
st.write(
    "Researchers and developers can access the MIMIC-III dataset by completing the necessary "
    "training and obtaining access through the PhysioNet website. More information on accessing the dataset can be found "
    "on the [MIMIC-III website](https://mimic.physionet.org/gettingstarted/access/)."
)

# Dataset Features
st.header("Key Features of the MIMIC-III Dataset")
st.write(
    "The MIMIC-III dataset includes a variety of features, such as:\n"
    "- Patient demographics\n"
    "- Vital signs (e.g., heart rate, blood pressure)\n"
    "- Laboratory test results\n"
    "- Medication orders and administrations\n"
    "- Diagnoses and procedures\n"
    "- Clinical notes and reports\n"
    "- And more."
)

# Data Usage and Citation
st.header("Data Usage and Citation")
st.write(
    "Users of the MIMIC-III dataset are expected to adhere to the data use agreement and cite the original "
    "publications associated with the dataset. Please refer to the [MIMIC-III citation page](https://mimic.physionet.org/about/cite/) "
    "for detailed information on citing the dataset in your work."
)

# Footer
st.write(
    "For more detailed information and documentation about the MIMIC-III dataset, please refer to the official "
    "[MIMIC-III website](https://mimic.physionet.org/). If you have any questions or inquiries, please contact the "
    "MIMIC-III research team through their [contact page](https://mimic.physionet.org/about/team/)."
)

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Page title
st.title("MIMIC-III Dataset Information and EDA")

# Introduction
st.write(
    "The MIMIC-III (Medical Information Mart for Intensive Care III) dataset is a publicly available dataset "
    "that contains de-identified health data for patients admitted to the intensive care unit (ICU). "
    "This page provides an overview of the MIMIC-III dataset along with a simple exploratory data analysis (EDA) visualization."
)

# Load a sample dataset (you can replace this with your actual MIMIC-III dataset)
# For demonstration purposes, let's assume the dataset contains a 'heart_rate' column
# with simulated data for heart rates of patients


viz1 = "main/assets/viz1.png"
viz2 = "main/assets/viz2.png"
viz3 = "main/assets/viz3.png"
viz4 = "main/assets/viz4.png"
viz5 = "main/assets/viz5.png"


# Visualization: Distribution of Heart Rates
st.header("Exploratory Data Analysis (EDA)")

# Plot the distribution of heart rates
st.subheader("Sepsis Patients by Gender")
st.image(viz1, caption="plot 1", use_column_width=False, width=500)
st.write("The distribution of sepsis patients by gender, with 56.2% being male and 43.8% female, ",
        "suggests a notable gender disparity in the prevalence of sepsis. ")

st.divider()
st.subheader("Death Among Sepsis Patients")
st.image(viz2, caption="plot 2", use_column_width=False, width=500)
st.write("The mortality rate of 25.3% indicates the proportion of sepsis patients in the dataset who did ",
        "not survive the condition. This is a critical metric for assessing the severity and impact of sepsis on the studied population.")

st.divider()
st.subheader("Ethnicities")
st.image(viz3, caption="plot 3", use_column_width=False, width=500)
st.write("The information about the distribution of ethnicities in the MIMIC dataset, with white being the most common, suggests a demographic ",
         "characteristic of the patient population represented in the dataset.")

st.divider()
st.subheader("Marital Status")
st.image(viz4, caption="plot 4", use_column_width=False, width=500)
st.write("The information about marital status among sepsis patients, with the majority being married, provides insights ",
         "into the demographic composition of the affected population.")

st.divider()
st.subheader("Insurance Type")
st.image(viz5, caption="plot 5", use_column_width=False, width=500)
st.write("The distribution of insurance types among sepsis patients reflects the various ways individuals are covered for ",
         "healthcare expenses. Medicare, in this case, is a government-sponsored insurance program primarily for individuals ",
         "aged 65 and older, and some younger individuals with certain disabilities.")

# Additional EDA visualizations can be added as needed

st.divider()
# Footer
st.write(
    "For more detailed information and documentation about the MIMIC-III dataset, please refer to the official "
    "[MIMIC-III website](https://mimic.physionet.org/). If you have any questions or inquiries, please contact the "
    "MIMIC-III research team through their [contact page](https://mimic.physionet.org/about/team/)."
)


text = "©2024 HFR Company. All rights reserved. The content on this website is protected by copyright law."
text2 = "For permission requests, please contact +6287870190448."

# Using HTML tags for text alignment
centered_text = f"<p style='text-align:center'>{text}</p>"
centered_text2 = f"<p style='text-align:center'>{text2}</p>"
st.divider()
# Displaying centered text using st.markdown
st.markdown(centered_text, unsafe_allow_html=True)
st.markdown(centered_text2, unsafe_allow_html=True)