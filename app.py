import cv2
import streamlit as st
import numpy as np
import time

st.title(" Invisible Cloak App")

start = st.button("Start Cloak", key="start_btn")
stop = st.button("Stop Cloak", key="stop_btn")

frame_window = st.image([])

if start:
    cap = cv2.VideoCapture(0)
    time.sleep(2)
    ret, background = cap.read()

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # blue cloak range
        lower_bound = np.array([90, 50, 50])
        upper_bound = np.array([130, 255, 255])
        mask = cv2.inRange(hsv, lower_bound, upper_bound)

        cloak = cv2.bitwise_and(background, background, mask=mask)
        inverse_mask = cv2.bitwise_not(mask)
        current_background = cv2.bitwise_and(frame, frame, mask=inverse_mask)
        combined = cv2.add(cloak, current_background)

        frame_window.image(combined, channels="BGR")

        # Stop if user clicks Stop Cloak
        if stop:
            break

    cap.release()
