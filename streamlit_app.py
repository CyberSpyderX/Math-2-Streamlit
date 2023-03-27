import cv2
from streamlit_webrtc import webrtc_streamer

webrtc_streamer(key="example", rtc_configuration={"iceServers": [{"urls": "stun:relay.metered.ca:80"}]})