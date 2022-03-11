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
                st.title(id_row.loc[0 , 'brand'] + ' ' + id_row.loc[0, 'model'])
                st.title(id_row.loc[0 , 'Price'])
                st.image(id_row.loc[0 , 'Image'])

                st.markdown("Release Year : " + str(id_row.loc[0, 'Release Year']))
                st.markdown("Display : " + id_row.loc[0, 'Display'])
                st.markdown("Weight : " + id_row.loc[0, 'Weight'])
                st.markdown("Graphics : " + id_row.loc[0, 'Graphic Card'])
                st.markdown("Processor : " + id_row.loc[0, 'Processor'])
                

            else:
                df = pandas.read_csv('assets/phones.csv') 

                id_row =  df.loc[df['ID'] == allids[0]]
                st.title(id_row.loc[0 , 'brand'] + ' ' + id_row.loc[0, 'model'])
                st.title(id_row.loc[0 , 'Price'])
                st.image(id_row.loc[0 , 'Image'])

                st.markdown("Release date : " + id_row.loc[0, 'release date'])
                st.markdown("Refresh rate : " + id_row.loc[0, 'Refresh Rate'] )
                st.markdown("Camera : " + id_row.loc[0, 'Camera'])
                st.markdown("Battery : " + id_row.loc[0, 'Battery'])
                st.markdown("Storage options : " + id_row.loc[0, 'Storage options'])
                st.markdown("Colours : " + id_row.loc[0, 'Colours'])
else:
    st.markdown(cur_object)


    








