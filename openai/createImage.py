import numpy as np
import cv2
image = np.zeros((500,500))
image[:,:]= 100
image = image[:,:]+10
image[100:200,200:300] = 255
image[400:500, 300:900] = 0
cv2.imwrite('./image/imgg.jpg',image)