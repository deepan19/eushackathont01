import fileinput
import streamlit as st
import numpy as np
from PIL import Image

st.title('Better Buy')

fileup = st.file_uploader("",type=["jpeg","jpg","png","jfif","webp"])

if fileup:

    image = Image.open(fileup)
    
    st.image(image, use_column_width=True)




