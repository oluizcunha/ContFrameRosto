import cv2
import os

BLUE_COLOR = (255, 0, 0)
STROKE = 2

xml_path = 'haarcascade_frontalface_alt2.xml'
clf = cv2.CascadeClassifier(xml_path)
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
l = 10
r = 20
contador= 0

while(not cv2.waitKey(20) & 0xFF == ord('q')):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = clf.detectMultiScale(gray)
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), BLUE_COLOR, STROKE)
        contador=contador+1
    cv2.putText(frame,"Frames com rostos: %d" %contador,(l,r),font,0.40,(0,0,255),1)
    
    cv2.imshow('frame', frame)
    

cap.release()
cv2.destroyAllWindows()
