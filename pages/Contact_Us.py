import streamlit as st
from send_email import send_email

st.header('Contact Me')

with st.form(key='contact_form'):
    user_email = st.text_input("Your email address")
    raw_message = st.text_area("Your Message")
    user_message = f"""\
Subject: A New Message from {user_email}
{raw_message}
From: {user_email}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(user_message)
        st.info("Your email was sent successfully")

