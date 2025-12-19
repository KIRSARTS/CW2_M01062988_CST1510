import streamlit as st
from app.tickets import get_all_it_tickets
from app.db import get_db_connection
import pandas as pd

conn = get_db_connection()
data = get_all_it_tickets(conn)

st.set_page_config(
    page_title='My Tickets',
    layout='wide'
)
if not st.session_state['logged_in']:
    st.warning("Please log in to access the dashboard.")
    st.stop()
    
    
st.title("Welcome to the Tickets Page")
st.write("Access all your ticket information here.")



with st.sidebar:
    st.header("Navigation")
    Priority = st.selectbox("Priority", data['priority'].unique())
    
filtered_data = data[data['priority'] == Priority]   


col1, col2 = st.columns(2)

with col1:
   st.subheader("Description") 
   st.bar_chart(filtered_data['description'].value_counts())

with col2:
    st.subheader("Ticket_ID over Time")
    st.line_chart(filtered_data, x ='resolution_time_hours', y = 'ticket_id')

st.subheader("Filtered Data")
st.dataframe(filtered_data)


 

