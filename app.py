import fileinput
import streamlit as st
import numpy as np
from PIL import Image
import cv2
import pyzbar.pyzbar as pyzbar
import pandas


frame_skip = 300
st.image('assets/BB-logo.jpg')

#run = st.checkbox('Scan')
run = st.slider('Scan', 0, 1, 1)

st.markdown(
    f'''
        <style>
            .sidebar .sidebar-content {{
                width: 375px;
            }}
        </style>
    ''',
    unsafe_allow_html=True
)

FRAME_WINDOW = st.image([])
camera = cv2.VideoCapture(0)

cur_frame = 0
cur_object = 'Stopped'

while run:
    _, frame = camera.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    FRAME_WINDOW.image(frame)
    decodedObjects = pyzbar.decode(frame)
    if len(decodedObjects) > 0:
        if(cur_object != decodedObjects[0].data.decode()):
            cur_object = decodedObjects[0].data.decode()
            
            device = cur_object.split('-',1)[0] == 'l'

            allids = cur_object.split('\n')

            if(device):
                df = pandas.read_csv('assets/laptops.csv')

                id_row =  df.loc[df['ID'] == allids[0]]
                st.title(id_row['Brand'] + ' ' + id_row['Model'])
                st.title(id_row['Price'])
                st.image(id_row['Image'])

                st.markdown("Release Year : " + id_row['Release Year'])
                st.markdown("Display : " + id_row['Display'])
                st.markdown("Weight : " + id_row['Weight'])
                st.markdown("Graphics : " + id_row['Graphic Card'])
                st.markdown("Processor : " + id_row['Processor'])
                

            else:
                df = pandas.read_csv('assets/phones.csv') 

                st.title(id_row['Brand'] + ' ' + id_row['Model'])
                st.title(id_row['Price'])
                st.image(id_row['Image'])

                st.markdown("Release date : " + id_row['Release date'])
                st.markdown("Camera : " + id_row['Camera'])
                st.markdown("Battery : " + id_row['Battery'])
                st.markdown("Storage options : " + id_row['Storage options'])
                st.markdown("Colours : " + id_row['Colours'])


            st.markdown()

            st.markdown(decodedObjects[0].data.decode())
else:
    st.markdown(cur_object)


    








