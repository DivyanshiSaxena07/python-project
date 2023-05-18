import cv2
import numpy as np
import matplotlib.pyplot as plt
import mediapipe as mp

mp_facemesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils
cordinate = mp_drawing._normalized_to_pixel_coordinates
all_lf_eye = list(mp_facemesh.FACEMESH_LEFT_EYE)
all_lf_eye = set(np.ravel(all_lf_eye))

all_rg_eye = list(mp_facemesh.FACEMESH_RIGHT_EYE)
all_rg_eye = set(np.ravel(all_rg_eye))

all_eye = all_lf_eye.union(all_rg_eye)

choosen_lf_eye = [362,385,387,263,373,380]
choosen_rg_eye = [33,160,158,133,153,144]

all_choosen = choosen_lf_eye + choosen_rg_eye


image = cv2.imread('./image/img3.jpg')
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
image =np.ascontiguousarray(image)
imgH, imgW, _ = image.shape

with mp_facemesh.FaceMesh(
  static_image_mode =True,
  max_num_faces = 1,
  refine_landmarks=False,
  min_detection_confidence=0.5,
  min_tracking_confidence=0.5
) as face_mesh:
  result =face_mesh.process(image)
  
landmark_0 = result.multi_face_landmarks[0].landmark[0]
print(landmark_0)
 
landmark_0_x = landmark_0.x * imgW 
landmark_0_y = landmark_0.y * imgH
landmark_0_z = landmark_0.z * imgW



def plot(*,img_dt,img_eye_lm = None,img_eye_lm_choose=None,face_lm=None,
         ts_tn=1,ts_c_r=2,l_c_r=3,name="1"):
    image_drawing_tool = img_dt
    img_eye_lm_choose=img_dt.copy() if img_eye_lm_choose is None else img_eye_lm_choose
    
    connections_drawing_spec=mp_drawing.DrawingSpec(
      thickness=ts_tn,
      circle_radius = ts_c_r,
      color=(255,255,255) 
    )
    fig = plt.figure(figsize=(20,15))
    fig.set_facecolor("white")
    
    mp_drawing.draw_landmarks(
      image = img_eye_lm_choose,
      landmark_list = face_landmarks,
      connections= mp_facemesh.FACEMESH_CONTOURS ,
      landmark_drawing_spec = None,
      connection_drawing_spec = connections_drawing_spec
      
    )
    lm = face_landmarks.landmark
    print(lm)
    for landmark_idx,landmark in enumerate(lm):
      if landmark_idx in all_eye:
        pred_code =cordinate(landmark.x,landmark.y,imgW, imgH)
        cv2.circle(img_eye_lm,pred_code,l_c_r,(255, 255, 255), -1 )
    
  
    plt.imshow(img_eye_lm_choose)
    plt.title("Chosen landmarks", fontsize=18)
    plt.axis("off")
    plt.show()
    plt.close()
    return

if result.multi_face_landmarks:
    for face_id, face_landmarks in enumerate(result.multi_face_landmarks):    
        _ = plot(img_dt=image.copy(), face_lm=face_landmarks)

# cv2.imshow("image",image)
# cv2.waitKey(0)