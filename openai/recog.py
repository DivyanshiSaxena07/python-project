import cv2

face_cap=cv2.CascadeClassifier('main_file/haar-cascade-files-master/haarcascade_frontalface_default.xml')
eye_cap=cv2.CascadeClassifier('main_file/haar-cascade-files-master/haarcascade_eye.xml')
cap=cv2.VideoCapture('vid22.mp4')
 
while True:
    ret, frame=cap.read()
    
    col=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors = 5, 
        minSize=(30,30),
        flags=cv2.CASCADE_SCALE_IMAGE
        
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h),(0,255,0),2)
        roi_gray=col[y:y+h, x:x+w]
        roi_color=frame[y:y+h, x:x+w]
        cv2.putText(frame,'face', org=(x,y), fontScale=0.8, color=(255, 0, 0), thickness=2, fontFace=cv2.LINE_AA)

        eyes=eye_cap.detectMultiScale(roi_gray)
        
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey), (ex+ew, ey+eh),(0,0,255) ,2)
            cv2.putText(roi_color,'eye', org=(ex,ey), fontScale=0.5, color=(25, 0, 0), thickness=2, fontFace=cv2.LINE_AA)
        
        
    if ret:
        cv2.imshow("Live Video", frame)
        if cv2.waitKey(2)==27:
            break

cap.release()
cv2.destroyAllWindows()