import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Mass Balance Calculator")

# Upload the CSV file
uploaded_file = st.file_uploader("Upload a file to calculate the mass balance for the measured stakes:", type='csv')

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("Data Preview")
    st.write(df.head())

    
if 'IceMelted (m)' in df.columns:
    df['stake.mb(m w.e)'] = df['IceMelted (m)'] * 0.9
    
    st.subheader("Stake mass balance")
    st.write(df)
    
# use matplotlib.pyplot to create a bar chart
    # fig, ax = ax.subplots()
    # ax.bar(df['Stake'], df['stake.mb(m w.e)'], color = 'red', edgecolor = 'k')
    
    # ax.set_xticks(df['Stake'])
    # ax.set_xlabel('Stake No.')
    # ax.set_ylabel('mass balance(m w.e.)')
    # ax.set_title('Stake mass balance')
    
    # st.pyplot(fig)
    
    st.divider()
    
    # Interactive bar chart
    st.bar_chart(df, x='Stake', y=['IceMelted (m)'],
                 x_label = "Stake No.", y_label = "Mass balance (m w.e.)",
                 color="#FF0000")
else:
    st.error("The uploaded error must have an 'IceMelted (m)' column.")
