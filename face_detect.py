import cv2
import numpy as np
face=cv2.CascadeClassifier(r'C:\Users\ANC\Desktop\xml\haarcascade_frontalface_default.xml')
eye=cv2.CascadeClassifier(r'C:\Users\ANC\Desktop\xml\haarcascade_eye.xml')
cap=cv2.VideoCapture(0)
while True:
    rec,frame=cap.read()
    frame_gr=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    facese=face.detectMultiScale(frame_gr,1.3,5 )
    eyes=eye.detectMultiScale(frame_gr,1.3,5)
    for (x,y,w,h)in facese:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,22,255),2)
        for(x,y,w,h) in eyes:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('live',frame)
    if cv2.waitKey(1)==13:
        break
cv2.destroyAllWindows()
cap.release()