import cv2
from streamlit_webrtc import webrtc_streamer, RTCConfiguration

webrtc_streamer(key="example", rtc_configuration=RTCConfiguration({"iceServers": [{"urls": "turn:relay.metered.ca:443?transport=tcp", "username": "6c6333babd32db890da89835", "credential": "qN6FOiA4TSmFzDu3"}]}))