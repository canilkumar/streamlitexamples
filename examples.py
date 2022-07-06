import streamlit as st
value = st.slider('val')  # this is a widget
st.write(value, 'squared is', value * value)

st.title('Welcome to Streamlit!')

checkbox_one = st.checkbox("Yes")

checkbox_two = st.checkbox("No")

if checkbox_one:
    value = "Yes"

elif checkbox_two:
      value = "No"
else:
      value = "No value selected" 

st.write(f"you selected: {value}")  