import streamlit as st
import pandas as pd

st.title("Place Based Allocation Tool")


@st.cache
def get_data():
    path = "~/Desktop/AIF/ICS Allocation Tool /gp_practice_weighted_population_by_ics v2.xlsx"
    return pd.read_excel(path, 1, 0, usecols="B,F,H,J,L,M,N:AC")


data = get_data()
data = data.rename(columns={"Region21_7": "Region", "STP21_42": "ICS", "GP practice name": "practice_name"})

ics = data['ICS'].drop_duplicates()
ics_choice = st.sidebar.selectbox("Select your ICS:", ics)
practices = list(data["practice_name"].loc[data["ICS"] == ics_choice])
practice_choice = st.sidebar.multiselect("Select practices", practices)

data.loc[(data['ICS'] == ics_choice) & (data['practice_name'].isin(practice_choice))]
