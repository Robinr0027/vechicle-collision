from camera import startapplication
import streamlit as st 
import os
from mail import send_sms

st.title('Collision Detection')

up_vdo = st.file_uploader('Upload Video', type=['mp4'])

if up_vdo is not None:
    with open(os.path.join(os.getcwd(), up_vdo.name), 'wb') as f:
        f.write(up_vdo.getvalue())
            
if st.button('Detect'):
    if up_vdo is not None:
        probs = startapplication(up_vdo.name)
        if (probs > 60) .any:
            st.write('Major Accident: Probability: {}'.format(probs))
            try:
                msg = 'Major accident detected'
                send_sms(msg)
            except:
                print("SMS NOT SENT")
        else:
            st.write('Not a Major Accident: Probability: {}'.format(probs))
    else:
        st.write('Please upload a video file.')