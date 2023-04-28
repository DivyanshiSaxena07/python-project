# import face_recognizer
# import cv2 
# import numpy as np
# import csv
# import os 
# import glob 
# from datetime import datetime

import face_recognizer
known_image = face_recognizer.load_image_file("https://upload.wikimedia.org/wikipedia/commons/c/c0/Official_Photograph_of_Prime_Minister_Narendra_Modi_Potrait.png")
unknown_image = face_recognizer.load_image_file("https://upload.wikimedia.org/wikipedia/commons/c/c0/Official_Photograph_of_Prime_Minister_Narendra_Modi_Potrait.png")

biden_encoding = face_recognizer.face_encodings(known_image)[0]
unknown_encoding = face_recognizer.face_encodings(unknown_image)[0]

results = face_recognizer.compare_faces([biden_encoding], unknown_encoding)

print(results)