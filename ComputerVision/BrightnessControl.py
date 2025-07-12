

# brightness Control Computer with OpenCv Python

import cv2                              #membuka kamera
import mediapipe as mp                  #mendeteksi tangan,titk kunci
from math import hypot                  #
import screen_brightness_control as sbc
import numpy as np                      #interpolasi np.interp

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')

camera = cv2.VideoCapture(0)
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    status, frame = camera.read()   #BGR
    # RGB
    imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)


    if not status:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    face = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,0,0), thickness=3)
        cv2.putText(frame, 'terdeteksi anak lelah', (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (0,128,0), thickness=5)


    lm_list = []
    if result.multi_hand_landmarks: # [] -> false, [nilai] -> trus
        for handlandmark in result.multi_hand_landmarks:
            for id, lm in enumerate(handlandmark.landmark):
                h, w, _, = frame.shape
                cx = int(lm.x*w)
                cy = int(lm.y*h)
                lm_list.append([id, cx, cy])
            
            mpDraw.draw_landmarks(frame, handlandmark, mpHands.HAND_CONNECTIONS)
    
    if lm_list != []:
        x1 = lm_list[4][1]
        y1 = lm_list[4][2]
        x2 = lm_list[8][1]
        y2 = lm_list[8][2]
        cv2.circle(frame, (x1, y1), 4, (255, 0, 0), thickness=-1)
        cv2.circle(frame, (x2, y2), 4, (255, 0, 0), thickness=-1)
        cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), thickness=3)
        hypotenuse = hypot(x2-x1, y2-y1)
        bright = np.interp(hypotenuse, [15, 200], [0, 100])     # 200 = 100%, 15 = 0%
        print(bright, hypotenuse)
        sbc.set_brightness(int(bright)) 

    cv2.imshow('Camera Bright Setting',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()

