import cv2
from streamlit_webrtc import webrtc_streamer

webrtc_streamer(key="example", rtc_configuration={"iceServers": [{"urls": "turn:relay.metered.ca:443", "username": "6c6333babd32db890da89835", "credential": "qN6FOiA4TSmFzDu3"}]})