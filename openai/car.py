import cv2

face_cap = cv2.CascadeClassifier('main_file/haar-cascade-files-master/haarcascade_car.xml')
cap = cv2.VideoCapture('car.mp4')

while True:
    ret,frame = cap.read()
    col = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale(col,1.3,5)
    
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        
    cv2.imshow("Live Video",frame)
    if cv2.waitKey(2)==27:
        break

cap.release()
cv2.destroyAllWindows()