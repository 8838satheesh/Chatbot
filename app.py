import streamlit as st
from auth import login, signup
from chatbot import get_answer
from database import init_db, save_chat, get_user_history
from utils import scrape_college_info
from admin import admin_view

st.set_page_config(page_title="TN College Chatbot")

init_db()

if 'user' not in st.session_state:
    st.session_state['user'] = None

menu = st.sidebar.selectbox("Menu", ["Login", "Signup", "Chat", "History", "Admin", "Logout"])

if menu == "Login" and not st.session_state['user']:
    login()
elif menu == "Signup" and not st.session_state['user']:
    signup()
elif menu == "Chat" and st.session_state['user']:
    st.subheader("Chat with College Bot")
    query = st.text_input("Ask about a college in Tamil Nadu:")
    if st.button("Send") and query:
        text_data = scrape_college_info()
        answer = get_answer(query, text_data)
        st.write(answer)
        save_chat(st.session_state['user']['id'], query, answer)
elif menu == "History" and st.session_state['user']:
    st.subheader("Chat History")
    history = get_user_history(st.session_state['user']['id'])
    for h in history:
        st.markdown(f"**Q:** {h[0]}\n\n**A:** {h[1]}\n\n*{h[2]}*")
elif menu == "Admin" and st.session_state['user'] and st.session_state['user']['role'] == 'admin':
    admin_view()
elif menu == "Logout":
    st.session_state['user'] = None
    st.success("Logged out successfully")
else:
    if not st.session_state['user']:
        st.warning("Please login to continue.")
