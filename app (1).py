import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Import the dataframe
df = pickle.load(open('df.pkl', 'rb'))
pipe = pickle.load(open('pipe.pkl', 'rb'))

# Add title
st.title('Laptop Price Predictor')

# Brand
company = st.selectbox('Brand', df['Company'].unique())

# Type of laptop
type = st.selectbox('Type', df['TypeName'].unique())

# RAM
ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])

# Weight
weight = st.number_input('Weight of the Laptop (in kg)')

# Touchscreen
touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])

# IPS
ips = st.selectbox('IPS', ['No', 'Yes'])

# 4k Display
display_4k = st.selectbox('4k display', ['No', 'Yes'])

# Full HD Display
full_hd = st.selectbox('Full HD Display', ['No', 'Yes'])


# Screen size
screen_size = st.number_input('Screen Size (in inches)',min_value=0.1)

# Resolution
resolution = st.selectbox('Screen Resolution',
                          ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600',
                           '2560x1440', '2304x1440'])

# CPU
cpu = st.selectbox('CPU', df['cpu brand'].unique())

# HDD
hdd = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])

# SSD
ssd = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])

# GPU
gpu = st.selectbox('GPU', df['gpubrand'].unique())

# OS
os = st.selectbox('OS', df['OpSysbrand'].unique())

# Create button
if st.button('Predict price'):
    ppi = None

    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else:
        ips = 0

    if display_4k == 'Yes':
        display_4k = 1
    else:
        display_4k = 0

    if full_hd == 'Yes':
        full_hd = 1
    else:
        full_hd = 0

    best_lambda = 0.11840251956086785

    x_res = int(resolution.split('x')[0])
    y_res = int(resolution.split('x')[1])
    ppi = ((x_res ** 2) + (y_res ** 2)) ** 0.5 / screen_size

    query = pd.DataFrame(
        [[company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd,
          gpu, os]],
        columns=['Company', 'TypeName', 'Ram', 'Weight', 'touchscreen', 'ips',
                 'ppi',  'cpu brand', 'HDD', 'SSD', 'gpubrand', 'OpSysbrand'])

    st.title("The predicted price of this laptop is " + str(
        int(np.exp(pipe.predict(query)[0]))))

    st.subheader('Fill the feedback form')
    feedback_form = """
        <form action="https://formsubmit.co/deyjoita19@gmail.com" method="POST">


    <input type="hidden" name="_captcha" value="false">  
    <input type="number" name="original_price" placeholder="Original Price" required>
    <input type="number" name="predict_price" placeholder="Predict Price" required>
    <button type="submit">Send</button>
    </form>
    """
    st.markdown(feedback_form, unsafe_allow_html=True)