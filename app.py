import streamlit as st
import os

st.title('Collision Detection')

up_vdo = st.file_uploader('Upload Video', type=['mp4'])

if up_vdo is not None:
    with open(os.path.join(os.getcwd(), up_vdo.name), 'wb') as f:
        f.write(up_vdo.getvalue())

if st.button('Detect'):
    os.system('python main.py')