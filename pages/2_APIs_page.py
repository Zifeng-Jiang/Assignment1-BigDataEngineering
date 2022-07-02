import numpy as np
import streamlit as st
import requests
import json

st.title('Airbus Ship Detection')
st.markdown("Using APIs")

APIs_name = ['run length decode', 'image contains certain number of ships', 'ship/nonship image', 'image and masks', 'num of ship in an image']
selected_API = st.selectbox("Choose which API to use: ", [i for i in APIs_name])
with st.form("api_form"):
    if selected_API == 'image contains certain number of ships':
        st.write("This function's purpose is to find out how many images in our dataset has certain number of ships.")
        st.write("You can select an integer number and you will get how many images in our dataset has this certain number of ships.")
        user_input = st.number_input('Please input number of ships in images: ', max_value = 15, min_value = 0, step = 1)
        submit = st.form_submit_button("Submit")
        if submit:
            res = requests.get(f"https://airbus-detection-data-services.herokuapp.com/image_number_of_ships/{user_input}")
            st.write(res.json())
    if selected_API == 'image and masks':
        st.write("This function's purpose is to find out the image numpy array and the mask array.")
        st.write("You can input any image file name in the dataset and you will get the numpy array and mask array of this image.")
        user_input = st.text_input('Image file name: ')
        submit = st.form_submit_button("Submit")
        if submit:
            res = requests.get(f"https://airbus-detection-data-services.herokuapp.com/image_and_masks/{user_input}")
            st.write(res.json())

    if selected_API == 'num of ship in an image':
        st.write("This function's purpose is to find out the num of ship(s) in an image.")
        st.write("You can input any image file name in the dataset and you will get how many ships are there in this image.")
        user_input = st.text_input('Image file name: ')
        submit = st.form_submit_button("Submit")
        if submit:
            res = requests.get(f"https://airbus-detection-data-services.herokuapp.com/num_ship_image/{user_input}")
            st.write(res.json())

    if selected_API  == 'run length decode':
        st.write("This function's purpose is to decode the run length encode.")
        st.write("You can input run length encoded pixels data and you will get the array for the image.")
        user_input = st.text_input('Run-length encoded pixels: ')
        submit = st.form_submit_button("Submit")
        if submit:
            res = requests.get(f"https://airbus-detection-data-services.herokuapp.com/run_length_decode/{user_input}")
            st.write(res.json())

    if selected_API == 'ship/nonship image':
        st.write("This function's purpose is to return a image array with or without ship.")
        st.write("You can input ship or noship and you will get the array for the image with or without ship correspondingly.")
        user_input = st.text_input('ship or noship: ')
        submit = st.form_submit_button("Submit")
        if submit:
            st.write(requests.get(f"https://airbus-detection-data-services.herokuapp.com/ship_nonship_image/{user_input}").json())