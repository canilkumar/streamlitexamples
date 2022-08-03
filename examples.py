import streamlit as st
st.title('Welcome to  Anil Kumar')
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
import tensorflow as tf

img_file_buffer = st.camera_input("Take a picture")

if img_file_buffer is not None:
    # To read image file buffer as a 3D uint8 tensor with TensorFlow:
    bytes_data = img_file_buffer.getvalue()
    img_tensor = tf.io.decode_image(bytes_data, channels=3)

    # Check the type of img_tensor:
    # Should output: <class 'tensorflow.python.framework.ops.EagerTensor'>
    st.write(type(img_tensor))

    # Check the shape of img_tensor:
    # Should output shape: (height, width, channels)
    st.write(img_tensor.shape)