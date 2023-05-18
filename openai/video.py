import cv2

cap=cv2.VideoCapture("vid22.mp4")
fourcc=cv2.VideoWriter_fourcc(*'MJPG')
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
fps = cap.get(cv2.CAP_PROP_FPS)
out = cv2.VideoWriter("vido.mp4",fourcc,fps,(int(width),int(height)))
if(cap.isOpened()):
    while(cap.isOpened()):
        ret, frame=cap.read()
        if(ret):
            cv2.imshow("video camera", frame)
            out.write(frame)
            
            if(cv2.waitKey(2)==27):
                break
out.release()
cap.release()
cv2.destroyAllWindows()