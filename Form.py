import streamlit as st
st.title("Collect the Data")
name = st.text_input ("Enter Your Name")
age = st.text_input("Enter You NAme")
district = st.selectbox("Select District", ("Ajmer","Alwar", "Banswara", "Barmer"))
button = st.button("Submit")
if button :
    st.chat_message("Submitted!")
