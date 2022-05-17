import streamlit as st

name = st.text_input("Enter your name",max_chars=10)
st.title(name)

password = st.text_input("Enter Password", type='password')
st.title(password)

message = st.text_area("Message", height=100)
st.title(message)

#number = st.number_input("Enter number", 0, 25, 6, 2)
#st.number(number)

#Date Input

my_date = st.date_input("Select date") 
st.write(my_date)

import datetime

#Date Input
my_date = st.date_input("Select date", value = datetime.date(1995, 6, 15), 
                          min_value = datetime.date(2020, 1, 1), 
                          max_value = datetime.date(2025, 12, 31))
st.write(my_date)

my_time = st.time_input("Select time")
st.write(my_time)

color = st.color_picker("Select Colour")
st.title(color)


