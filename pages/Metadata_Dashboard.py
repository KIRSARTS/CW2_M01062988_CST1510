import streamlit as st
from app.metadata import get_all_datasets_metadata
from app.db import get_db_connection
import pandas as pd


conn = get_db_connection()
data = get_all_datasets_metadata(conn)

st.set_page_config(
    page_title='My Data',
    layout='wide'
)
if not st.session_state['logged_in']:
    st.warning("Please log in to access the dashboard.")
    st.stop()
    
st.title("Welcome to the Database Page")
st.write("Access all your database information here.")


col1, col2 = st.columns(2)


with st.sidebar:
    st.header("Navigation")
    dataset_id= st.selectbox("Dataset_ID", data['dataset_id'].unique())
    
    filtered_data = data[data['dataset_id'] == dataset_id]
    
   
    
with col1:
    st.subheader("Uploaded Data")
    st.bar_chart(filtered_data['uploaded_by'].value_counts())
    
   
with col2:
    st.subheader("Name over Rows")
    st.line_chart(filtered_data, x ='rows', y = 'name') 
    
st.subheader("Filtered Data")     
st.dataframe(filtered_data)