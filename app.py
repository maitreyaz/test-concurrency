import streamlit as st
import os

# Set the directory to save uploaded files
UPLOAD_DIR = 'uploads'
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

# Streamlit app
st.title("PDF Upload App")

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Save the uploaded file to the uploads directory
    save_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
    
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success(f"File saved to {save_path}")
