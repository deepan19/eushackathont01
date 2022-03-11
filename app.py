import fileinput
import streamlit as st
import numpy as np
import sys, qrcode
from PIL import Image
import cv2

st.title('Better Buy')

fileup = st.file_uploader("",type=["jpeg","jpg","png","jfif","webp"])

if fileup:

    image = Image.open(fileup)
    
    st.image(image, use_column_width=True)

    qrCodeDetector = cv2.QRCodeDetector()

    decodedText, points, _ = qrCodeDetector.detectAndDecode(image)

    if points is not None:
 
        nrOfPoints = len(points)
    
        for i in range(nrOfPoints):
            nextPointIndex = (i+1) % nrOfPoints
            cv2.line(image, tuple(points[i][0]), tuple(points[nextPointIndex][0]), (255,0,0), 5)
    
        print(decodedText)    
    
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
     
    else:
        print("QR code not detected")



    








