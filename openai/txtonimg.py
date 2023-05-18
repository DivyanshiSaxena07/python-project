# import cv2

# img_get = cv2.imread(r"/home/dev/Desktop/divyanshi/openai/image/img1.jpg")
# img_get = cv2.resize(img_get,(500,600))

# txt = cv2.putText(img = img_get,
# text = "laptop",
# org = (50,100),
# fontFace = cv2.FONT_HERSHEY_DUPLEX,
# fontScale = 2,
# color = (0,0,0),
# thickness = 3,
# lineType=cv2.LINE_8)



# cv2.imshow("laptop",txt)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


import cv2 
img_get = cv2.imread(r"/home/dev/Desktop/divyanshi/openai/image/img1.jpg",cv2.IMREAD_GRAYSCALE)
img_get = cv2.resize(img_get,(500,600))

txt = cv2.putText(img= img_get,text = "coffie",org=(250,60),fontFace=cv2.FONT_HERSHEY_DUPLEX,fontScale=2,
color=(255,0,0),
thickness=2,
lineType=cv2.LINE_8)

image = cv2.circle(img_get,center=(120,100),radius=30,color=(0,0,255),thickness=-1)

# cv2.imshow("Laptop",txt)
cv2.imshow("Laptop",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

