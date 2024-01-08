# Import necessary libraries
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pickle as pkl
import pandas as pd
from itertools import product

with open('/Users/family/Documents/GitHub/ICU-Deployment/What I need. maybe?/dqn_normal_actions_test.p', 'rb') as file:
    agent_action_test = pkl.load(file)

with open('/Users/family/Documents/GitHub/ICU-Deployment/What I need. maybe?/sarsa_phys/phys_actions_test.p', 'rb') as file:
    phys_action_test = pkl.load(file)

data = pd.read_csv('/Users/family/Documents/GitHub/ICU-Deployment/What I need. maybe?/rl_test_data_final_cont.csv')

# Page title
st.title("Demo")
st.divider()
# Introduction
st.write(
    "This page demonstrates a simple prediction using a hypothetical machine learning model. "
)

options = data['icustayid'].drop_duplicates()
# Create a combo box using selectbox
selected_option = st.selectbox("Select an ICU Stay ID:", options)

# Display the selected option
st.write(f"You selected: {selected_option}")
st.divider()
#def show_table(selected_state):


# Button to trigger prediction
if st.button("Predict"):
    st.subheader("Dose Intensity Recomendation for The Patients")
    save_indexes = []
    i_index = 0
    for i, row in data.iterrows():
        if data.loc[i, 'icustayid'] == selected_option:
            save_indexes.append(i)
    
    phys_act = []
    ai_act = []
    vaso_phys = []
    iv_phys = []
    vaso_ai = []
    iv_ai = []
    doses_intensity = ["Zero", "Low", "Medium", "High", "Very High"]
    pair_of_act = list(product(doses_intensity, repeat=2))
    st.divider()
    # Your loop to fill the data
    for i in range(len(save_indexes)):
        st.text(f"Dose Intensity After {(i+1)*4} Hour")
        phys_act.append(pair_of_act[phys_action_test[save_indexes[i]]])
        ai_act.append(pair_of_act[agent_action_test[save_indexes[i]]])
        vaso_phys.append(phys_act[i][0])
        iv_phys.append(phys_act[i][1])
        vaso_ai.append(ai_act[i][0])
        iv_ai.append(ai_act[i][1])
        temp = {
            'IV Fluid': {'Physician': phys_act[i][0], 'AI': ai_act[i][0]},
            'Vasopressor': {'Physician': phys_act[i][1], 'AI': ai_act[i][1]}
        }
        df = pd.DataFrame(temp)
        st.table(df)
        st.divider()

    # Data
    #doses_intensity_set1 = ['High', 'Low', 'Zero', 'High', 'High', 'Low']
    #doses_intensity_set2 = ['Medium', 'High', 'Low', 'Medium', 'High', 'Medium']
    y_labels = ["Zero", "Low", "Medium", "High", "Very High"]

    # Map doses_intensity to corresponding numerical values
    y_values_set1 = [y_labels.index(intensity) for intensity in vaso_phys]
    y_values_set2 = [y_labels.index(intensity) for intensity in vaso_ai]

    # Create a line plot for each set
    plt.plot(range(len(vaso_phys)), y_values_set1, label='Physician', marker='o', linestyle='-')
    plt.plot(range(len(vaso_ai)), y_values_set2, label='AI', marker='o', linestyle='-')

    # Customize the plot
    plt.xlabel('Index 4-Hourly Timestamps')
    plt.ylabel('Intensity')
    plt.title('Vasopressor Doses Intensity Line Plot')
    plt.yticks(range(len(y_labels)), y_labels)
    plt.legend()
    st.pyplot(plt)

    #show_sofa = st.checkbox("SOFA Score")
    #show_gcs = st.checkbox("GCS")
    # Conditionally display text based on the checkbox value
    selected_param = ["SOFA", "GCS", "SIRS", "Temp_C", "SysBP", "DiaBP", "HR"]
    show_table = data[selected_param]
    show_table = show_table.loc[save_indexes].reset_index(drop=True)
    plt.figure(figsize=(10, 6))
    plt.plot(show_table['SOFA'], label='SOFA')
    plt.plot(show_table['GCS'], label='GCS')
    plt.plot(show_table['SIRS'], label='SIRS')
    plt.plot(show_table['Temp_C'], label='Temperature (C)')
    plt.plot(show_table['SysBP'], label='SysBP')
    plt.plot(show_table['DiaBP'], label='DiaBP')
    plt.plot(show_table['HR'], label='Heart Rate')

    # Customize the plot
    plt.xlabel('Time')
    plt.ylabel('Normalized Values')
    plt.title('Parameters Over Time')
    plt.legend()
    plt.grid(True)
    st.pyplot(plt)
    #if show_sofa:
    #    selected_param.append("SOFA")
    #else:
    #    selected_param.remove("SOFA")
    #st.write(selected_param)
        
        

    # Creating a DataFrame
    #df = pd.DataFrame(data)

    # Displaying the table in Streamlit
    #st.table(df)
    #st.write(f"{save_indexes}")

# Footer



