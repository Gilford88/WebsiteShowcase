import streamlit as st
import send_email

st.header('Contact Me')

with st.form(key='contact_form'):
    user_email = st.text_input("Your email address")
    user_message = st.text_area("Your Message")
    button = st.form_submit_button("Submit")
    if button:

