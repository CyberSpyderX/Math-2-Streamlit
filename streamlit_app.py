import cv2
import numpy as np
import keras
import streamlit as st
from keras.preprocessing import image
from keras.utils import load_img, img_to_array
import time


st.title("Webcam Live Feed")

run = st.checkbox('Start')
FRAME_WINDOW = st.image([])


def nothing1(x):
    pass


image_x, image_y = 64, 64
from keras.models import load_model


classifier = load_model(r'Handgesture_Final_CNN_d_26_march.h5')


def predictor():
    from keras import backend as K
    import numpy as np
    # from keras.preprocessing import image
    test_image = load_img(r"1.jpg",target_size=(64, 64))
    test_image = img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    #classifier = load_model(r'G:\\Code_dataset\Handgesture_Final_FCN.h5')
    #classifier = load_model(r'G:\\Code_dataset\Handgesture_Final_VGG16.h5')

    result = classifier.predict(test_image)
    K.clear_session()
   # print(result)
    if result[0][0] == max(result[0]):
        return ' Zero  '
    elif result[0][1] == max(result[0]):
        return ' One  '
    elif result[0][2] == max(result[0]):
        return ' Two  '
    elif result[0][3] == max(result[0]):
        return ' Three  '
    elif result[0][4] == max(result[0]):
        return '  Four  '
    elif result[0][5] == max(result[0]):
        return 'Five'
    elif result[0][6] == max(result[0]):
        return 'Six'
    elif result[0][7] == max(result[0]):
        return 'Seven'
    elif result[0][8] == max(result[0]):
        return 'Eight'
    elif result[0][9] == max(result[0]):
        return 'Nine'
    elif result[0][10] == max(result[0]):
        return 'A'
    elif result[0][11] == max(result[0]):
        return 'B'
    elif result[0][12] == max(result[0]):
        return 'C'
    elif result[0][13] == max(result[0]):
        return 'D'
    elif result[0][14] == max(result[0]):
        return 'E'
    elif result[0][15] == max(result[0]):
        return 'F'
    elif result[0][16] == max(result[0]):
        return 'I'
    elif result[0][17] == max(result[0]):
        return 'J'
    elif result[0][18] == max(result[0]):
        return 'K'
    elif result[0][19] == max(result[0]):
        return 'L'
    elif result[0][20] == max(result[0]):
        return 'U'
    elif result[0][21] == max(result[0]):
        return 'M'
    elif result[0][22] == max(result[0]):
        return 'N'
    elif result[0][23] == max(result[0]):
        return 'O'
    elif result[0][24] == max(result[0]):
        return 'P'
    elif result[0][26] == max(result[0]):
        return 'Q'
    elif result[0][27] == max(result[0]):
        return 'R'
    elif result[0][28] == max(result[0]):
        return 'S'
    elif result[0][29] == max(result[0]):
        return 'T'
    elif result[0][30] == max(result[0]):
        return 'U'
    elif result[0][31] == max(result[0]):
        return 'V'
    elif result[0][32] == max(result[0]):
        return 'W'
    elif result[0][33] == max(result[0]):
        return 'X'
    elif result[0][34] == max(result[0]):
        return 'Y'
    elif result[0][35] == max(result[0]):
        return 'Z'

while run:
    picture = st.camera_input("Take a picture")

    bytes_data = picture.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
    st.write(cv2_img)
    time.sleep(5)