import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Title and description
st.title("Image Processing - Blur Effect")
st.write("This web application applies a blur effect to your image. Upload an image and choose the blur intensity.")

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Read the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert the image to an OpenCV-compatible format
    image_array = np.array(image)
    if image_array.shape[-1] == 4:  # Check for alpha channel
        image_array = cv2.cvtColor(image_array, cv2.COLOR_BGRA2BGR)

    # Slider for blur intensity
    blur_intensity = st.slider("Select blur intensity (kernel size)", 1, 50, 5)

    # Apply blur effect
    if blur_intensity % 2 == 0:  # Ensure kernel size is odd
        blur_intensity += 1
    blurred_image = cv2.GaussianBlur(image_array, (blur_intensity, blur_intensity), 0)

    # Display the blurred image
    st.image(blurred_image, caption="Blurred Image", use_column_width=True)
else:
    st.write("Please upload an image to proceed.")
