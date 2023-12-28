# Import necessary libraries
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pickle as pkl
import pandas as pd

with open('/Users/family/Documents/GitHub/ICU-Deployment/What I need. maybe?/dqn_normal_actions_test.p', 'rb') as file:
    agent_action_test = pkl.load(file)

with open('/Users/family/Documents/GitHub/ICU-Deployment/What I need. maybe?/sarsa_phys/phys_actions_test.p', 'rb') as file:
    phys_action_test = pkl.load(file)

data = pd.read_csv('/Users/family/Documents/GitHub/ICU-Deployment/What I need. maybe?/rl_test_data_final_cont.csv')

# Page title
st.title("Demo")

# Introduction
st.write(
    "This page demonstrates a simple prediction using a hypothetical machine learning model. "
)

options = data['icustayid'].drop_duplicates()
# Create a combo box using selectbox
selected_option = st.selectbox("Select an ICU Stay ID:", options)

# Display the selected option
st.write(f"You selected: {selected_option}")

#def show_table(selected_state):


# Button to trigger prediction
if st.button("Predict"):
    save_indexes = []
    i_index = 0
    for i, row in data.iterrows():
        if data.loc[i, 'icustayid'] == selected_option:
            save_indexes.append(i)
    
    phys_act = []
    ai_act = []
    #ivfluid_dose = ['0', '>0-40', '40-205', '205-635', '>635']
    #vaso_dose = ['0', '>0-0.110', '0.110-0.225', '0.225-0.450', '>0.450']
    actions = ['0 ml dose of iv fluid and 0 ug/kg/h dose of vasopressor',
              '0 ml dose of iv fluid and >0-0.110 ug/kg/h dose of vasopressor',
              '0 ml dose of iv fluid and 0.110-0.225 ug/kg/h dose of vasopressor',
              '0 ml dose of iv fluid and 0.225-0.450 ug/kg/h dose of vasopressor',
              '0 ml dose of iv fluid and >0.450 ug/kg/h dose of vasopressor',
              '>0-40 ml dose of iv fluid and 0 ug/kg/h dose of vasopressor',
              '>0-40 ml dose of iv fluid and >0-0.110 ug/kg/h dose of vasopressor',
              '>0-40 ml dose of iv fluid and 0.110-0.225 ug/kg/h dose of vasopressor',
              '>0-40 ml dose of iv fluid and 0.225-0.450 ug/kg/h dose of vasopressor',
              '>0-40 ml dose of iv fluid and >0.450 ug/kg/h dose of vasopressor',
              '40-205 ml dose of iv fluid and 0 ug/kg/h dose of vasopressor',
              '40-205 ml dose of iv fluid and >0-0.110 ug/kg/h dose of vasopressor',
              '40-205 ml dose of iv fluid and 0.110-0.225 ug/kg/h dose of vasopressor',
              '40-205 ml dose of iv fluid and 0.225-0.450 ug/kg/h dose of vasopressor',
              '40-205 ml dose of iv fluid and >0.450 ug/kg/h dose of vasopressor',
              '205-635 ml dose of iv fluid and 0 ug/kg/h dose of vasopressor',
              '205-635 ml dose of iv fluid and >0-0.110 ug/kg/h dose of vasopressor',
              '205-635 ml dose of iv fluid and 0.110-0.225 ug/kg/h dose of vasopressor',
              '205-635 ml dose of iv fluid and 0.225-0.450 ug/kg/h dose of vasopressor',
              '205-635 ml dose of iv fluid and >0.450 ug/kg/h dose of vasopressor',
              '>635 ml dose of iv fluid and 0 ug/kg/h dose of vasopressor',
              '>635 ml dose of iv fluid and >0-0.110 ug/kg/h dose of vasopressor',
              '>635 ml dose of iv fluid and 0.110-0.225 ug/kg/h dose of vasopressor',
              '>635 ml dose of iv fluid and 0.225-0.450 ug/kg/h dose of vasopressor',
              '>635 ml dose of iv fluid and >0.450 ug/kg/h dose of vasopressor',]
    for i in range(len(save_indexes)):
        phys_act.append(phys_action_test[save_indexes[i]])
        st.write(f"Physician action is giving {actions[phys_act[i]]}")
        ai_act.append(agent_action_test[save_indexes[i]])
        st.write(f"AI action is giving {actions[ai_act[i]]}")
        st.write("=====================================================================================\n")

    # Data
    x = range(len(ai_act))  # Assume ai_act and phys_act have the same length
    y1 = ai_act
    y2 = phys_act

    # Plotting garis
    plt.plot(x, y1, label='AI', marker='o')
    plt.plot(x, y2, label='Physician', marker='o')

    # Adding a y-axis range up to 24
    plt.ylim(0, 24)

    # Adding labels and title
    plt.xlabel('State')
    plt.ylabel('Choosen Action ')
    plt.title('Dose of IV fluid & Vasopressor Combination')

    # Adding a legend
    plt.legend()

    # Adding a grid
    plt.grid(True)

    # Displaying the plot using st.pyplot
    st.pyplot(plt)

    #show_sofa = st.checkbox("SOFA Score")
    #show_gcs = st.checkbox("GCS")
    # Conditionally display text based on the checkbox value
    selected_param = ["SOFA", "GCS", "SIRS", "Temp_C", "SysBP", "DiaBP", "HR"]
    show_table = data[selected_param]
    show_table = show_table.loc[save_indexes].reset_index(drop=True)
    st.write("Collection of patient states")
    st.table(show_table)
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
st.write(
    "Note: This is a demo and the prediction result may not be meaningful without a trained model. "
    "Replace the model loading and prediction logic with your actual machine learning model."
)


