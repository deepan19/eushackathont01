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

<<<<<<< Updated upstream
=======
st.markdown('<style>body{background-color: #2a4cba;}</style>',unsafe_allow_html=True)
>>>>>>> Stashed changes
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
                st.title(id_row.loc[id_row.index.values[0] , 'brand'] + ' ' + id_row.loc[id_row.index.values[0], 'model'])
                st.header(id_row.loc[id_row.index.values[0] , 'Price'])
                st.image(id_row.loc[id_row.index.values[0] , 'Image'])

                st.subheader('Release Year : ' + str(id_row.loc[id_row.index.values[0], 'Release Year']))
                st.subheader("Display : " + id_row.loc[id_row.index.values[0], 'Display'])
                st.subheader("Weight : " + id_row.loc[id_row.index.values[0], 'Weight'])
                st.subheader("Graphics : " + id_row.loc[id_row.index.values[0], 'Graphic Card'])
                st.subheader("Processor : " + id_row.loc[id_row.index.values[0], 'Processor'])
                st.title("------------------------------------------------")
                

            else:
                df = pandas.read_csv('assets/phones.csv') 

                id_row =  df.loc[df['ID'] == allids[0]]
                st.title(id_row.loc[id_row.index.values[0] , 'brand'] + ' ' + id_row.loc[id_row.index.values[0], 'model'])
                st.header(id_row.loc[id_row.index.values[0] , 'Price'])
                st.image(id_row.loc[id_row.index.values[0] , 'Image'])

                st.subheader("Release date : " + id_row.loc[id_row.index.values[0], 'release date'])
                st.subheader("Refresh rate : " + id_row.loc[id_row.index.values[0], 'Refresh Rate'] )
                st.subheader("Camera : " + id_row.loc[id_row.index.values[0], 'Camera'])
                st.subheader("Battery : " + id_row.loc[id_row.index.values[0], 'Battery'])
                st.subheader("Storage options : " + id_row.loc[id_row.index.values[0], 'Storage options'])
                st.subheader("Colours : " + id_row.loc[id_row.index.values[0], 'Colours'])
                st.title("------------------------------------------------")


else:
    st.markdown(cur_object)
    