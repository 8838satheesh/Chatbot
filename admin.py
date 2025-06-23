import streamlit as st
from database import create_connection

def admin_view():
    st.subheader("Admin Panel")
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    for u in users:
        st.write(u)
