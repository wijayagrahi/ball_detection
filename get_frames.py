# Python program to open the camera in Tkinter
# Import the libraries, tkinter, cv2, Image and ImageTk

from tkinter import *
import cv2
from PIL import Image, ImageTk

import numpy as np

# Define a video capture object
#vid_object = True
#vid = cv2.VideoCapture(0)

# Declare the width and height in variables
width, height = 800, 600

# Set the width and height
#vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
#vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)



video_capture_released = False

def release_video_capture():
    global vid, video_capture_released
    if video_capture_released:
        vid.release()
        video_capture_released = False

# Function to create and return a Tkinter frame
def get_images(current_detection_parameters):
    global vid, video_capture_released

    print(current_detection_parameters)

    # Check if video capture is released, and reinitialize if needed
    if not video_capture_released:
        vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        video_capture_released = True

    print(current_detection_parameters)
    #button1.configure(state="disabled")
    # Capture the video frame by frame
    _, frame = vid.read()

    #code for detections

    # Get current trackbar positions
    lower_h = current_detection_parameters['lower_h']
    lower_s = current_detection_parameters['lower_s']
    lower_v = current_detection_parameters['lower_v']
    upper_h = current_detection_parameters['upper_h']
    upper_s = current_detection_parameters['upper_s']
    upper_v = current_detection_parameters['upper_v']
    ker = current_detection_parameters['kernel']
    blur = current_detection_parameters['blur']
    radius_limit = current_detection_parameters['radius']



    frame = cv2.blur(frame, (blur, blur))

    lower_bound = np.array([lower_h, lower_s, lower_v])
    upper_bound = np.array([upper_h, upper_s, upper_v])

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    kernel = np.ones((ker, ker), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    #cv2.imshow("Hsv", mask)

    contours, hierarchy = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame, (0, 360), (1280, 360), (0, 177, 0), 2)

    if len(contours) > 0:
        c = max(contours, key=cv2.contourArea)
        (x, y), radius = cv2.minEnclosingCircle(c)
        center = (int(x), int(y))

        radius = int(radius)
        if radius > radius_limit:
            cv2.circle(frame, center, radius, (0, 255, 0), 2)
            cv2.circle(frame, center, 1, (0, 0, 255), 2)




    # Convert image from one color space to other
    opencv_image_left = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

    #for hsv
    #opencv_image = mask

    # Capture the latest frame and transform it to an image
    captured_image_left = Image.fromarray(opencv_image_left)



    # Convert captured image to PhotoImage
    photo_image_left = ImageTk.PhotoImage(image=captured_image_left)


    # for hsv
    opencv_image_right = mask

    # Capture the latest frame and transform it to an image
    captured_image_right = Image.fromarray(opencv_image_right)

    # Convert captured image to PhotoImage
    photo_image_right = ImageTk.PhotoImage(image=captured_image_right)

    return photo_image_left, photo_image_right




