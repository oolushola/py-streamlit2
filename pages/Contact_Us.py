import streamlit as st
import mailer
import pandas as pd


st.set_page_config(layout="wide")

topics = pd.read_csv("topics.csv")

myTopics = []
for index, data in topics.iterrows():
    myTopics.append(data["topic"])

st.header("Contact Us")
with st.form(key="contactUs"):
    receiver = st.text_input("Your Email Address")
    subject = st.selectbox("What topic do you want to discuss?", myTopics)

    message = st.text_area("Message")
    button = st.form_submit_button("Send")
    if button:
        mailer.sendEmail(message, receiver, subject)
        st.info("Message sent successfully")
