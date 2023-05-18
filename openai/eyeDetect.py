import cv2
import mediapipe as mp
import dlib
from imutils import face_utils

cap = cv2.VideoCapture("facevideo.mp4")
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmark.dat")

