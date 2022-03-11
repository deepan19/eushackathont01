import fileinput
import streamlit as st
import numpy as np
from PIL import Image
import cv2
import pyzbar.pyzbar as pyzbar


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
            st.markdown(decodedObjects[0].data.decode())
else:
    st.markdown(cur_object)


    








