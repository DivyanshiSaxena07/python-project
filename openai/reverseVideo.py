import cv2 
cap = cv2.VideoCapture('v1.mp4')
frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps = cap.get(cv2.CAP_PROP_FPS)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')

out = cv2.VideoWriter('reversed.mp4',fourcc,fps,(int(width*0.5),int(height*0.5)))

print("no of frames:{}".format(frames))
print("FPS is:{}".format(fps))

frame_idx = frames-1

if(cap.isOpened()):
    while(frame_idx!=0):
        cap.set(cv2.CAP_PROP_POS_FRAMES,frame_idx)
        ret, frame = cap.read()
        frame = cv2.resize(frame,(int(width*0.5),int(height*0.5)))
        out.write(frame)
        frame_idx =frame_idx-1
        
        if(frame_idx%100==0):
            print(frame_idx)

out.release()            
cap.release()
cv2.destroyAllWindows()
