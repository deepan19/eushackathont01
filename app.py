import fileinput
import streamlit as st
import numpy as np
from PIL import Image
import cv2

st.title('Better Buy')

fileup = st.file_uploader("",type=["jpeg","jpg","png","jfif","webp"])

if fileup:

    image = np.array(Image.open(fileup))
    
    qrCodeDetector = cv2.QRCodeDetector()

    decodedText, points, _ = qrCodeDetector.detectAndDecode(image)

    if points is not None:
        st.markdown(decodedText)
     
    else:
        print("QR code not detected")



    








