import cv2  
import numpy as np
import matplotlib.pyplot as plt
import requests
from PIL import Image

image = cv2.imread('Tom.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(gray, cmap='gray'), plt.show()

def convert2RGB(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

face = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
face_c = face.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5);print('Faces Found', len(face_c))

for(x_face, y_face, w_face, h_face) in face_c:
    cv2.rectangle(image, (x_face,y_face), (x_face + w_face, y_face + w_face), (0,0,255),10)
plt.imshow(convert2RGB(image)), plt.show()