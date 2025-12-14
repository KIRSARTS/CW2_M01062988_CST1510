import streamlit as st
from app.incidence import get_all_cyber_incidents
from app.db import get_db_connection
import pandas as pd

conn = get_db_connection()
data = get_all_cyber_incidents(conn)


st.set_page_config(
    page_title='My Incidents',
    layout='wide'
)

if not st.session_state['logged_in']:
    st.warning("Please log in to access the dashboard.")
    st.stop()

st.title("Welcome to the Home Page")
st.write("This is the main landing page of the application.")
st.write("Access all your information on Incidents here.")

data['timestamp'] = pd.to_datetime(data['timestamp'])

with st.sidebar:
    st.header("Navigation")
    severity_ = st.selectbox("Severity", data['severity'].unique())

filtered_data = data[data['severity'] == severity_]
    
col1, col2 = st.columns(2)

with col1:
   st.bar_chart(filtered_data['category'].value_counts())

with col2:
    st.line_chart(filtered_data, x ='timestamp', y = 'incident_id')


st.dataframe(filtered_data)