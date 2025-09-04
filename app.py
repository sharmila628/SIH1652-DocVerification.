import streamlit as st
import easyocr
import cv2
import numpy as np

st.title("📄 Document Verification System")

uploaded_file = st.file_uploader("Upload a document image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    st.image(image, channels="BGR")

    reader = easyocr.Reader(['en'])
    result = reader.readtext(image)

    st.subheader("🔍 Extracted Text")
    for (bbox, text, prob) in result:
        st.write(f"{text} (confidence: {prob:.2f})")
