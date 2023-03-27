import cv2
import streamlit as st

def main():
    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)

    # Set the resolution of the webcam
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    st.title("Webcam Test")

    # Use a loop to continuously read frames from the webcam
    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        if not ret:
            st.text('The camera could not be opened')
            break

        # Convert the frame to RGB color space
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display the frame in Streamlit
        st.image(frame, channels="RGB")

        # Check if the user has pressed the 'Esc' key
        if cv2.waitKey(1) == 27:
            break

    # Release the VideoCapture object and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()