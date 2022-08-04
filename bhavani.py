import streamlit as st
st.title('Welcome to  Lakshmi Bhavani Channamsetti')
st.subheader('How are you?')
st.subheader('what about your parents')
select_status = st.sidebar.radio("Select Any One", ('Value for truth',
'Value for money', 'value for love', 'value for mothers love'))
st.write(f"you selected: {select_status}")
color = st.select_slider(
     'Select a color of the rainbow',
     options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write('My favorite color is', color)