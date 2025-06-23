import streamlit as st
from database import insert_user, get_user

def signup():
    st.subheader("Signup")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Register"):
        try:
            insert_user(username, password)
            st.success("Signup successful! Please log in.")
        except:
            st.error("Username already exists.")

def login():
    st.subheader("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = get_user(username, password)
        if user:
            st.session_state['user'] = {'id': user[0], 'username': user[1], 'role': user[3]}
            st.success(f"Welcome {user[1]}")
        else:
            st.error("Invalid credentials")
