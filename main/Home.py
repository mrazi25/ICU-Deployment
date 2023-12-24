
# Import necessary libraries
import streamlit as st
import base64


def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )


autoplay_audio("/Users/family/Documents/GitHub/ICU-Deployment/main/assets/background-music.mp3")
st.title("Sepvisor")

# Project description
st.write(
    "Welcome to the Sepsis Treatment Recommendation app. This application "
    "provides recommendations for sepsis treatment based on several clinical parameters."
)

# What is sepsis?
st.header("What is Sepsis?")
st.write(
    "Sepsis is a severe illness caused by the body's response to an infection. It can lead to organ "
    "failure and, if not treated promptly, can be fatal. Early detection and intervention are crucial "
    "for successful treatment."
)

# Symptoms of sepsis
st.header("Symptoms of Sepsis")
st.write(
    "Sepsis symptoms can vary, but common signs include fever, elevated heart rate, rapid breathing, "
    "confusion, and extreme discomfort. If you suspect sepsis, seek medical attention immediately."
)

# Risk factors
st.header("Risk Factors")
st.write(
    "Certain factors increase the risk of developing sepsis, including age, weakened immune system, "
    "chronic medical conditions, and recent surgery or invasive procedures."
)

# Prevention and treatment
st.header("Prevention and Treatment")
st.write(
    "Preventing infections, practicing good hygiene, and seeking prompt medical attention for infections "
    "can help prevent sepsis. Treatment involves antibiotics, supportive care, and addressing the underlying cause."
)

# Additional resources or links
st.header("Additional Resources")
st.write(
    "For more detailed information and resources about sepsis, you can visit the following websites:"
)
st.markdown(
    "- [Sepsis Alliance](https://www.sepsis.org/)\n"
    "- [World Health Organization (WHO) - Sepsis](https://www.who.int/news-room/questions-and-answers/item/sepsis)\n"
    "- [Centers for Disease Control and Prevention (CDC) - Sepsis](https://www.cdc.gov/sepsis/index.html)"
)

# Footer
st.write(
    "This information hub is created using Streamlit. If you have any questions or feedback, please "
    "contact [Your Name] at [Your Email Address]."
)
