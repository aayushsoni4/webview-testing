import streamlit as st
import cv2
from PIL import Image
import numpy as np

# Set page config to wide mode
st.set_page_config(layout="wide")

# Hide all default elements and remove margins/padding
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stApp { 
    max-width: 100%;
    padding: 0;
    margin: 0;
}
.block-container {
    max-width: 100%;
    padding: 0;
    margin: 0;
}
.stCamera {
    margin: 0;
    padding: 0;
}
.stCamera > label {
    display: none;
}
div[data-testid="stVerticalBlock"] {
    padding: 0;
    margin: 0;
}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Create a video capture object without title
video_capture = st.camera_input(label="Camera", key="camera", label_visibility="hidden")

if video_capture is not None:
    # Open the image using PIL
    image = Image.open(video_capture)
    
    # Convert PIL Image to numpy array
    img_array = np.array(image)
    
    # Flip the image horizontally
    flipped_img = cv2.flip(img_array, 1)
    
    # Display the flipped image in full width without padding
    st.image(flipped_img, channels="RGB", use_column_width=True)