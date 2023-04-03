import cv2
face = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

cape = cv2.VideoCapture('elon.MP4')

while True:
    _,img =cape.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray,1.1,4)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 5) 
    cv2.imshow('Video',img)

    k=cv2.waitKey(30) & 0xff
    if k==27:
        break
cape.release()