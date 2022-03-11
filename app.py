import streamlit as st
import numpy as np
from PIL import Image

st.title('Better Buy')

picture = st.camera_input("Take a picture")

if picture:
    st.image(picture)




