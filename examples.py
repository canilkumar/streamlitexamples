import streamlit as st
st.title('Welcome to  Kurma Grace Nandini')
value = st.slider('val')  # this is a widget
st.write(value, 'squared is', value * value)



checkbox_one = st.checkbox("Yes")

checkbox_two = st.checkbox("No")

if checkbox_one:
    value = "Yes"

elif checkbox_two:
      value = "No"
else:
      value = "No value selected" 

st.write(f"You selected: {value}")  

select_box = st.sidebar.selectbox(

    "Select Yes or No",
    ["Yes", "No"]
)
st.write(f"You selected: {select_box}")

select_status = st.sidebar.radio("Covid-19 patient's status", ('Confirmed',
'Active', 'Recovered', 'Deceased'))
st.write(f"Covid-19 patient's status: {select_status}")
picture = st.camera_input("Take a picture")

if picture:
     st.image(picture)