import streamlit as st
from appl import hash_password, validate_hash
from app.users import add_user, get_user
from app.db import get_db_connection

conn = get_db_connection()

st.title("Welcome to the Home Page")
st.write("This is the main landing page of the application.")


if'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False


tab_login, tab_register = st.tabs(["Login", "Register"])

with tab_login:
    login_username = st.text_input("Username")
    login_password = st.text_input("Password", type = "password")
    
    if st.button("Log In"):
        id, name, password = get_user(conn, login_username)
        if not validate_hash(login_password, password):
            st.error("Invalid username or password. Please try again.")
        else:
            st.session_state['logged_in'] = True
            st.success("You are now logged in.")
          
   
# password registration
with tab_register:
    register_username = st.text_input("New Username")
    register_password = st.text_input("New password", type = "password")
    
if st.button("Register"):
    hash_password = hash_password(register_password)
    add_user(conn, register_username, hash_password)  
    st.success("You have registered successsfully. Please log in")


st.session_state











