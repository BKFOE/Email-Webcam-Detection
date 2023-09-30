import cv2
from datetime import datetime
import streamlit as st


st.title("Motion Detector")
start = st.button("Start Camera")

if start:
    streamlit_image = st.image([])
    video = cv2.VideoCapture(0)

    while True:
        check, frame = video.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        d = datetime.now()

        cv2.putText(frame, d.strftime("%A"), (50, 50), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(0, 255, 0),
                    thickness=4, lineType=cv2.LINE_AA)
        cv2.putText(frame, d.strftime("%H:%M:%S"), (50, 80), fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(0, 255, 0),
                    thickness=4, lineType=cv2.LINE_AA)

        streamlit_image.image(frame)

