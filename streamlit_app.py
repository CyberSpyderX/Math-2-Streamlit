import cv2
from streamlit_webrtc import webrtc_streamer, RTCConfiguration

webrtc_streamer(key="example", rtc_configuration=RTCConfiguration({ "iceServers": [{"urls": ["stun:stun1.l.google.com:19302"]}]}))